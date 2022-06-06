import os
from flask import redirect, request, url_for
from flask_admin import form
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_security import url_for_security
from flask_admin.contrib import sqla
from markupsafe import Markup
from sqlalchemy.event import listens_for

from app import path, Image


class MySuperUserModelView(ModelView):
    column_exclude_list = ['image']

    def is_accessible(self):
        return current_user.has_role('SuperUser')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for_security('login', next=request.url))


class MyAdminModelView(sqla.ModelView):
    column_exclude_list = ['password', 'image']
    # column_searchable_list = ['Address', ]
    column_labels = dict(street='Улица', house='№ дома', price='Цена', district='Район', away_settlement='Удалённое заселение',
                         numbers_of_room='Количество комнат', type_of_room='Тип комнат', total_space='Общая площадь',
                         space_of_kitchen='Площадь кухни', space_of_living='Жилая площадь', furniture='Мебель',
                         technics='Техника', balcony_or_loggia='Балкон или лоджия', ceiling_height='Высота потолков',
                         bathroom='Сан узел', widow='Окна', repair='Ремонт', floor='Этаж', description='Описание',
                         timestamp='Дата создания', name='Название фото', path='Фото', image='К какой квартире принадлежит')

    def is_accessible(self):
        return current_user.has_role('SuperUser') or current_user.has_role('Admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for_security('login', next=request.url))


class ImageModelView(sqla.ModelView):
    column_labels = dict(name='Название фото', path='Фото', image='К какой квартире принадлежит')
    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=path,
                                      thumbnail_size=(100, 100, True))
    }

    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''
        return Markup('<img src="%s">' % url_for('static',
                                                 filename=('ImageFlat/' + form.thumbgen_filename(model.path))))

    column_formatters = {
        'path': _list_thumbnail
    }


@listens_for(Image, 'after_delete')
def del_image(mapper, connection, target):
    if target.path:
        # Delete image
        try:
            os.remove(os.path.join(path, target.path))
        except OSError:
            pass

        # Delete thumbnail
        try:
            os.remove(os.path.join(path, form.thumbgen_filename(target.path)))
        except OSError:
            pass