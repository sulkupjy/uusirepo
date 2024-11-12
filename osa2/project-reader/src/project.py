class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return "\n-  "+"\n-  ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nlicense: {self.license}"
            f"\n\n\nauthors: {self._stringify_dependencies(self.authors)}"
            f"\n\n\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\n\n\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
