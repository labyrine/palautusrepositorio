class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def __str__(self):
        project = (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}\n\n"
        )
        project += "Authors:\n"
        project += "\n".join([f"- {author}" for author in self.authors]) + "\n\n"
        project += "Dependencies:\n"
        project += "\n".join([f"- {dependency}" for dependency in self.dependencies]) + "\n\n"
        project += "Development dependencies:\n"
        project += "\n".join([f"- {dev_dependency}" for dev_dependency in self.dev_dependencies])
        
        return project
