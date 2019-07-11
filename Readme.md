# Cross Database Foreign Key

[![Build Status](https://travis-ci.com/SelfHacked/django-crossdb-foreignkey.svg?branch=master)](https://travis-ci.com/SelfHacked/django-crossdb-foreignkey)
[![Coverage Status](https://coveralls.io/repos/github/varuna-sd/django-crossdb-foreignkey/badge.svg?branch=master)](https://coveralls.io/github/varuna-sd/django-crossdb-foreignkey?branch=master)

Cross database foreign key is used when models in different databases needs to be related with each other. Django only have limited support for cross database foreign keys and this library is designed to extend that support.


## Usage

#### Configure the Database Router

Enable cross database relationships using Django database router (https://docs.djangoproject.com/en/2.2/topics/db/multi-db/#topics-db-multi-db-routing).

Make sure that relations are allowed between objects by enabling relations ships in `allow_relation` functions of the Router.

#### Define relationships

Use `CrossDBForeignKey` and `CrossDBOneToOneField` to define cross database relationships.

#### Example

```
# Department is in the 'Management' database
class Department(models.Model):
    code = models.CharField(max_length=6)


# Employee is in the 'HR' database
class Employee(models.Model):
    name = models.TextField()
    department = CrossDBForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='employees',
    )
```


## Limitations of cross database foreign keys

- Does not support queries spanning to multiple models in different databases.
- Support only CASCADE, SET_NULL, and DO_NOTHING for on_delete.
