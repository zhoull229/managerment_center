# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SBCommonRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SBCommonRequest.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n$com.wd.proto.base.operating_platformB\021CustomerRoleProtoP\001'),
  serialized_pb=_b('\n\x15SBCommonRequest.proto\"M\n\x0c\x43ustomerRole\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08roleName\x18\x02 \x01(\t\x12\x1f\n\nmoduleRela\x18\x03 \x03(\x0b\x32\x0b.ModuleRela\"\x89\x01\n\x07\x45\x64ition\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rschoolGradeId\x18\x02 \x01(\t\x12\x11\n\tsubjectId\x18\x03 \x01(\t\x12\x0f\n\x07pressId\x18\x04 \x01(\t\x12\x11\n\tpressName\x18\x05 \x01(\t\x12\x12\n\nfascicleId\x18\x06 \x01(\t\x12\x10\n\x08\x63overUrl\x18\x07 \x01(\t\"O\n\tLoginUser\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08userName\x18\x02 \x01(\t\x12\x10\n\x08schoolId\x18\x03 \x01(\t\x12\x12\n\naccessCode\x18\x04 \x01(\t\"M\n\nModuleRela\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nmoduleName\x18\x02 \x01(\t\x12\x1f\n\nmoduleRela\x18\x03 \x03(\x0b\x32\x0b.ModuleRela\"&\n\x05Press\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tpressName\x18\x02 \x01(\t\">\n\x0bSchoolGrade\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tgradeName\x18\x02 \x01(\t\x12\x10\n\x08schoolId\x18\x03 \x01(\t\"z\n\x12SchoolGradeSubject\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bsubjectName\x18\x02 \x01(\t\x12\x15\n\rschoolGradeId\x18\x03 \x01(\t\x12\x1e\n\x16schoolingLengthGradeId\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\t\"Z\n\x0fSchoolingLength\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x1b\n\x13schoolingLengthName\x18\x03 \x01(\t\x12\x10\n\x08schoolId\x18\x04 \x01(\t\"T\n\x1aSchoolingLengthSchoolGrade\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tgradeName\x18\x02 \x01(\t\x12\x17\n\x0fschoolingLength\x18\x03 \x01(\t\"Z\n\x07Subject\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08schoolId\x18\x02 \x01(\t\x12\x13\n\x0bsubjectName\x18\x03 \x01(\t\x12\x0e\n\x06staged\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\t\"F\n\x12SubjectSchoolGrade\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tsubjectId\x18\x02 \x01(\t\x12\x11\n\tgradeName\x18\x03 \x01(\tB;\n$com.wd.proto.base.operating_platformB\x11\x43ustomerRoleProtoP\x01\x62\x06proto3')
)




_CUSTOMERROLE = _descriptor.Descriptor(
  name='CustomerRole',
  full_name='CustomerRole',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CustomerRole.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roleName', full_name='CustomerRole.roleName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moduleRela', full_name='CustomerRole.moduleRela', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=102,
)


_EDITION = _descriptor.Descriptor(
  name='Edition',
  full_name='Edition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Edition.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolGradeId', full_name='Edition.schoolGradeId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subjectId', full_name='Edition.subjectId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pressId', full_name='Edition.pressId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pressName', full_name='Edition.pressName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fascicleId', full_name='Edition.fascicleId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coverUrl', full_name='Edition.coverUrl', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=242,
)


_LOGINUSER = _descriptor.Descriptor(
  name='LoginUser',
  full_name='LoginUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='LoginUser.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userName', full_name='LoginUser.userName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolId', full_name='LoginUser.schoolId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accessCode', full_name='LoginUser.accessCode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=244,
  serialized_end=323,
)


_MODULERELA = _descriptor.Descriptor(
  name='ModuleRela',
  full_name='ModuleRela',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ModuleRela.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moduleName', full_name='ModuleRela.moduleName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moduleRela', full_name='ModuleRela.moduleRela', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=402,
)


_PRESS = _descriptor.Descriptor(
  name='Press',
  full_name='Press',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Press.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pressName', full_name='Press.pressName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=404,
  serialized_end=442,
)


_SCHOOLGRADE = _descriptor.Descriptor(
  name='SchoolGrade',
  full_name='SchoolGrade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SchoolGrade.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gradeName', full_name='SchoolGrade.gradeName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolId', full_name='SchoolGrade.schoolId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=444,
  serialized_end=506,
)


_SCHOOLGRADESUBJECT = _descriptor.Descriptor(
  name='SchoolGradeSubject',
  full_name='SchoolGradeSubject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SchoolGradeSubject.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subjectName', full_name='SchoolGradeSubject.subjectName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolGradeId', full_name='SchoolGradeSubject.schoolGradeId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolingLengthGradeId', full_name='SchoolGradeSubject.schoolingLengthGradeId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='SchoolGradeSubject.code', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=630,
)


_SCHOOLINGLENGTH = _descriptor.Descriptor(
  name='SchoolingLength',
  full_name='SchoolingLength',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SchoolingLength.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='SchoolingLength.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolingLengthName', full_name='SchoolingLength.schoolingLengthName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolId', full_name='SchoolingLength.schoolId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=632,
  serialized_end=722,
)


_SCHOOLINGLENGTHSCHOOLGRADE = _descriptor.Descriptor(
  name='SchoolingLengthSchoolGrade',
  full_name='SchoolingLengthSchoolGrade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SchoolingLengthSchoolGrade.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gradeName', full_name='SchoolingLengthSchoolGrade.gradeName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolingLength', full_name='SchoolingLengthSchoolGrade.schoolingLength', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=724,
  serialized_end=808,
)


_SUBJECT = _descriptor.Descriptor(
  name='Subject',
  full_name='Subject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Subject.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolId', full_name='Subject.schoolId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subjectName', full_name='Subject.subjectName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='staged', full_name='Subject.staged', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='Subject.code', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=810,
  serialized_end=900,
)


_SUBJECTSCHOOLGRADE = _descriptor.Descriptor(
  name='SubjectSchoolGrade',
  full_name='SubjectSchoolGrade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SubjectSchoolGrade.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subjectId', full_name='SubjectSchoolGrade.subjectId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gradeName', full_name='SubjectSchoolGrade.gradeName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=902,
  serialized_end=972,
)

_CUSTOMERROLE.fields_by_name['moduleRela'].message_type = _MODULERELA
_MODULERELA.fields_by_name['moduleRela'].message_type = _MODULERELA
DESCRIPTOR.message_types_by_name['CustomerRole'] = _CUSTOMERROLE
DESCRIPTOR.message_types_by_name['Edition'] = _EDITION
DESCRIPTOR.message_types_by_name['LoginUser'] = _LOGINUSER
DESCRIPTOR.message_types_by_name['ModuleRela'] = _MODULERELA
DESCRIPTOR.message_types_by_name['Press'] = _PRESS
DESCRIPTOR.message_types_by_name['SchoolGrade'] = _SCHOOLGRADE
DESCRIPTOR.message_types_by_name['SchoolGradeSubject'] = _SCHOOLGRADESUBJECT
DESCRIPTOR.message_types_by_name['SchoolingLength'] = _SCHOOLINGLENGTH
DESCRIPTOR.message_types_by_name['SchoolingLengthSchoolGrade'] = _SCHOOLINGLENGTHSCHOOLGRADE
DESCRIPTOR.message_types_by_name['Subject'] = _SUBJECT
DESCRIPTOR.message_types_by_name['SubjectSchoolGrade'] = _SUBJECTSCHOOLGRADE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomerRole = _reflection.GeneratedProtocolMessageType('CustomerRole', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMERROLE,
  __module__ = 'SBCommonRequest_pb2'
  # @@protoc_insertion_point(class_scope:CustomerRole)
  ))
_sym_db.RegisterMessage(CustomerRole)

Edition = _reflection.GeneratedProtocolMessageType('Edition', (_message.Message,), dict(
  DESCRIPTOR = _EDITION,
  __module__ = 'SBCommonRequest_pb2'
  # @@protoc_insertion_point(class_scope:Edition)
  ))
_sym_db.RegisterMessage(Edition)

LoginUser = _reflection.GeneratedProtocolMessageType('LoginUser', (_message.Message,), dict(
  DESCRIPTOR = _LOGINUSER,
  __module__ = 'SBCommonRequest_pb2'
  # @@protoc_insertion_point(class_scope:LoginUser)
  ))
_sym_db.RegisterMessage(LoginUser)

ModuleRela = _reflection.GeneratedProtocolMessageType('ModuleRela', (_message.Message,), dict(
  DESCRIPTOR = _MODULERELA,
  __module__ = 'SBCommonRequest_pb2'
  # @@protoc_insertion_point(class_scope:ModuleRela)
  ))
_sym_db.RegisterMessage(ModuleRela)

Press = _reflection.GeneratedProtocolMessageType('Press', (_message.Message,), dict(
  DESCRIPTOR = _PRESS,
  __module__ = 'SBCommonRequest_pb2'
  # @@protoc_insertion_point(class_scope:Press)
  ))
_sym_db.RegisterMessage(Press)

SchoolGrade = _reflection.GeneratedProtocolMessageType('SchoolGrade', (_message.Message,), dict(
  DESCRIPTOR = _SCHOOLGRADE,
  __module__ = 'SBCommonRequest_pb2'
  # @@protoc_insertion_point(class_scope:SchoolGrade)
  ))
_sym_db.RegisterMessage(SchoolGrade)

SchoolGradeSubject = _reflection.GeneratedProtocolMessageType('SchoolGradeSubject', (_message.Message,), dict(
  DESCRIPTOR = _SCHOOLGRADESUBJECT,
  __module__ = 'SBCommonRequest_pb2'
  # @@protoc_insertion_point(class_scope:SchoolGradeSubject)
  ))
_sym_db.RegisterMessage(SchoolGradeSubject)

SchoolingLength = _reflection.GeneratedProtocolMessageType('SchoolingLength', (_message.Message,), dict(
  DESCRIPTOR = _SCHOOLINGLENGTH,
  __module__ = 'SBCommonRequest_pb2'
  # @@protoc_insertion_point(class_scope:SchoolingLength)
  ))
_sym_db.RegisterMessage(SchoolingLength)

SchoolingLengthSchoolGrade = _reflection.GeneratedProtocolMessageType('SchoolingLengthSchoolGrade', (_message.Message,), dict(
  DESCRIPTOR = _SCHOOLINGLENGTHSCHOOLGRADE,
  __module__ = 'SBCommonRequest_pb2'
  # @@protoc_insertion_point(class_scope:SchoolingLengthSchoolGrade)
  ))
_sym_db.RegisterMessage(SchoolingLengthSchoolGrade)

Subject = _reflection.GeneratedProtocolMessageType('Subject', (_message.Message,), dict(
  DESCRIPTOR = _SUBJECT,
  __module__ = 'SBCommonRequest_pb2'
  # @@protoc_insertion_point(class_scope:Subject)
  ))
_sym_db.RegisterMessage(Subject)

SubjectSchoolGrade = _reflection.GeneratedProtocolMessageType('SubjectSchoolGrade', (_message.Message,), dict(
  DESCRIPTOR = _SUBJECTSCHOOLGRADE,
  __module__ = 'SBCommonRequest_pb2'
  # @@protoc_insertion_point(class_scope:SubjectSchoolGrade)
  ))
_sym_db.RegisterMessage(SubjectSchoolGrade)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
