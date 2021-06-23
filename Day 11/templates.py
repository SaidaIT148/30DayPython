import os

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")


class Templates:
    template_name = ""
    context = None

    def __init__(self, template_name="", context=None, *args, **kwargs):
        self.template_name = template_name
        self.context = context

    def get_template(self):
        template_path = os.path.join(TEMPLATE_DIR, self.template_name)
        if not os.path.exists(template_path):
            raise Exception("This path does not exists")

        template_string = ""
        with open(template_path, "r") as f:
            template_string = f.read()
        return template_string

    def render(self, context=None):
        render_ctx = {}

        if self.context != None:
            render_ctx = self.context
        else:
            render_ctx = context

        if not isinstance(render_ctx, dict):
            render_ctx = {}

        template_string = self.get_template()

        # {:name":"saida"} or {name = "Saida"}
        return template_string.format(**render_ctx)
