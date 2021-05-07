import ast
import glob
from collections import defaultdict


def get_py_files(root_dir):
    result = list()
    for filename in glob.iglob(root_dir + '**/*.py', recursive=True):
        result.append(filename)
    return result


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


class UnusedImportChecker(ast.NodeVisitor):
    def __init__(self):
        self.filename = str()
        self.import_map = defaultdict(set)
        self.name_map = defaultdict(set)

    def _add_imports(self, node):
        for import_name in node.names:
            name = import_name.name
            self.import_map[self.filename].add((name, node.lineno))

    def visit_Import(self, node):
        self._add_imports(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.name_map[self.filename].add(node.id)

    def check(self, work_dir):
        filepaths = get_py_files(work_dir)
        for filepath in filepaths:
            self.filename = filepath
            tree = ast.parse(read_file(filepath))
            self.visit(tree)

    def report(self):
        for path, imports in self.import_map.items():
            for name, line in imports:
                if name not in self.name_map[path]:
                    print(f'{path}: {line} unused import "{name}"')


work_dir = 'analyze_me'
checker = UnusedImportChecker()
checker.check(work_dir)
checker.report()
