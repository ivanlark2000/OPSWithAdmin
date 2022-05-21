from app import app
from flask import abort, url_for, request, redirect, render_template
from flask_admin.contrib import sqla
from flask_login import current_user


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# Create customized model view class
class MyModelView(sqla.ModelView):
    # def is_accessible(self):
    #     return (current_user.is_active and
    #             current_user.is_authenticated
    #     )

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))