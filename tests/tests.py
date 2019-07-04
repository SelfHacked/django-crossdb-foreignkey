from django.test import TestCase
from example_models.models import (
    Department, OtherEmployee, OtherManager, OtherSection, OtherHeadOffice,
)


class SimpleModelTest(TestCase):

    databases = '__all__'

    def setUp(self):
        self._department_1 = Department(code='K001')
        self._department_1.save()

        self._employee_s = OtherEmployee(
            name='Smith',
            department=self._department_1,
        )
        self._employee_s.save()

        self._employee_k = OtherEmployee(
            name='Kevin',
            department=self._department_1,
        )
        self._employee_k.save()

        self._manager = OtherManager(
            name='Nancy',
            department=self._department_1,
        )
        self._manager.save()

        self._section = OtherSection(
            department=self._department_1,
        )
        self._section.save()

        self._headoffice = OtherHeadOffice(
            department=self._department_1,
        )
        self._headoffice.save()

        self._department_2 = Department(code='K002')
        self._department_2.save()
        self._employee_d = OtherEmployee(
            name='Damith',
            department=self._department_2,
        )
        self._employee_d.save()

    def test_create_with_foreignkey(self):
        """Test creation."""
        department = Department(code='D001')
        department.save()

        employee = OtherEmployee(name='John', department=department)
        employee.save()

        self.assertIn(employee, department.employees.all())

    def test_create_with_onetoone(self):
        """Test creation."""
        department = Department(code='D001')
        department.save()

        manager = OtherManager(name='John', department=department)
        manager.save()

        self.assertEqual(department.manager, manager)

    def test_list_linked_objects(self):
        """Test that linked objects could be listed"""
        self.assertEqual(2, len(self._department_1.employees.all()))
        self.assertIn(self._employee_s, self._department_1.employees.all())

    def test_query_with_foreign_key_not_supported(self):
        """Foreign key doesn't support queries."""
        with self.assertRaises(Exception):
            list(OtherEmployee.objects.filter(department__code='K002').all())

    def test_cascade_delete(self):
        """Test delete."""
        self._department_1.delete()
        employees = OtherEmployee.objects.all()

        self.assertNotIn(self._employee_s, employees)
        self.assertNotIn(self._employee_k, employees)

    def test_do_nothing_delete(self):
        """Test delete."""
        self._department_1.delete()
        managers = OtherManager.objects.all()

        self.assertIn(self._manager, managers)

    def test_delete_with_no_reverse(self):
        """Test delete."""
        self._department_1.delete()
        sections = OtherSection.objects.all()

        self.assertNotIn(self._section, sections)

    def test_delete_with_null_set(self):
        """Test delete."""
        self._department_1.delete()
        headoffice = OtherHeadOffice.objects.get(id=self._headoffice.id)

        self.assertIsNone(headoffice.department)
