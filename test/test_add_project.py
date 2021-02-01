from model.project import Project


def test_add_project(app, db, json_project, check_ui):
    project = json_project
    old_projects = db.get_project_list()
    app.project.create(project)
    new_projects = db.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

    def clean(cleaning_project):
        return Project(identifier=cleaning_project.identifier, name=cleaning_project.name.strip(),
                       description=cleaning_project.description.strip())
    if check_ui:
        clean_new_projects = map(clean, new_projects)
        assert sorted(clean_new_projects, key=Project.id_or_max) == sorted(app.project.get_project_list(), key=Project.id_or_max)
