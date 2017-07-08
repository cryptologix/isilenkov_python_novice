from model.classes import Group

def test_modife_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="new dasdasdasdas"))
    app.session.logout()

def test_modife_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="new header"))
    app.session.logout()

def test_modife_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(footer="new footer"))
    app.session.logout()


