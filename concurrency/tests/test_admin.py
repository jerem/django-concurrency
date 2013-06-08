# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth.models import User
from django_dynamic_fixture import G
from django_webtest import WebTest
from concurrency.admin import ConcurrentModelAdmin
from concurrency.tests.models import ConcurrentModel


class ConcurrentModelAdminTest(ConcurrentModelAdmin):
    ordering = ('id', )


class TestAdmin(WebTest):
    def setUp(self):
        super(TestAdmin, self).setUp()
        self.user = G(User, is_superuser=True,
                      is_staff=True,
                      is_active=True,
                      email='sax@example.com',
                      username='sax')
        G(ConcurrentModel, pk=1)
        G(ConcurrentModel, n=10, version=0)
        try:
            admin.site.unregister(ConcurrentModel)
        except NotRegistered:
            pass
        admin.site.register(ConcurrentModel, ConcurrentModelAdminTest)

    def test_delete_allowed_if_no_updates(self):
        res = self.app.get('/admin/', user='sax')
        res = res.click('ConcurrentModels')
        assert 'ConcurrentModel #1' in res  # sanity check

        form = res.forms['changelist-form']
        form['action'].value = 'delete_selected'
        sel = form.get('_selected_action', index=0)
        sel.checked = True
        res = form.submit()
        assert 'Are you sure?' in res
        assert 'ConcurrentModel #1' in res
        res = res.form.submit()
        self.assertNotIn('ConcurrentModel #1', res)

    def test_delete_not_allowed_if_updates(self):
        res = self.app.get('/admin/', user='sax')
        res = res.click('ConcurrentModels')
        assert 'ConcurrentModel #1' in res  # sanity check
        # update record to create conflict
        u = ConcurrentModel.objects.get(pk=1)
        u.dummy_char = 'charfield'
        u.save()

        form = res.forms['changelist-form']
        form['action'].value = 'delete_selected'
        sel = form.get('_selected_action', index=0)
        sel.checked = True
        res = form.submit().follow()
        self.assertIn('One or more record were updated', res)
