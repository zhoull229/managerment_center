# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ServerPrivilegeService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ServerCommonMessage_pb2 as ServerCommonMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ServerPrivilegeService.proto',
  package='platformserver',
  syntax='proto3',
  serialized_options=_b('\n1com.szwdcloud.platformserver.proto.platformserverB\033ServerPrivilegeServiceProtoP\001'),
  serialized_pb=_b('\n\x1cServerPrivilegeService.proto\x12\x0eplatformserver\x1a\x19ServerCommonMessage.proto\"w\n\x14PrivilegeSaveRequest\x12\x10\n\x08parentId\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x16\n\x0esystemCategory\x18\x05 \x01(\x05\x12\x0c\n\x04type\x18\x06 \x01(\x05\x12\x0b\n\x03url\x18\x07 \x01(\t\"\x99\x01\n\x16PrivilegeUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08parentId\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x12\n\nmoduleName\x18\x05 \x01(\t\x12\x16\n\x0esystemCategory\x18\x06 \x01(\x05\x12\x0c\n\x04type\x18\x07 \x01(\x05\x12\x0b\n\x03url\x18\x08 \x01(\t\"J\n\x10\x46indChildRequest\x12\x10\n\x08systemId\x18\x01 \x01(\x05\x12\x10\n\x08parentid\x18\x02 \x01(\t\x12\x12\n\nparentName\x18\x03 \x01(\t\"v\n\x0f\x46indChildResult\x12<\n\tprivilege\x18\x01 \x03(\x0b\x32).platformserver.FindChildResult.Privilege\x1a%\n\tPrivilege\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"$\n\x16PrivilegeDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\"7\n\x15\x46indPrivilegesRequest\x12\x10\n\x08systemId\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\"\xbb\x01\n\x14\x46indPrivilegesResult\x12\x41\n\tprivilege\x18\x01 \x03(\x0b\x32..platformserver.FindPrivilegesResult.Privilege\x1a`\n\tPrivilege\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x10\n\x08parentId\x18\x06 \x01(\t\"n\n\x17\x46indAllPrivilegeRequest\x12\x10\n\x08systemId\x18\x01 \x01(\t\x12\x0e\n\x06module\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x0e\n\x06pageNo\x18\x04 \x01(\x05\x12\x10\n\x08pageSize\x18\x05 \x01(\x05\"\xfd\x01\n\x16\x46indAllPrivilegeResult\x12\x43\n\tprivilege\x18\x01 \x03(\x0b\x32\x30.platformserver.FindAllPrivilegeResult.Privilege\x12\r\n\x05total\x18\x02 \x01(\x03\x12\r\n\x05pages\x18\x03 \x01(\x05\x12\x0e\n\x06pageNo\x18\x04 \x01(\x05\x12\x10\n\x08pageSize\x18\x05 \x01(\x05\x1a^\n\tPrivilege\x12\n\n\x02id\x18\x06 \x01(\t\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06module\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\x0b\n\x03url\x18\x05 \x01(\t\"\x1c\n\x0e\x46indOneRequest\x12\n\n\x02id\x18\x01 \x01(\t\"w\n\rFindOneResult\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x10\n\x08systemId\x18\x06 \x01(\x05\x12\x11\n\tparentIds\x18\x07 \x03(\t2\xaf\x04\n\x16ServerPrivilegeService\x12\x46\n\x04save\x12$.platformserver.PrivilegeSaveRequest\x1a\x18.platformserver.Response\x12J\n\x06update\x12&.platformserver.PrivilegeUpdateRequest\x1a\x18.platformserver.Response\x12J\n\x06\x64\x65lete\x12&.platformserver.PrivilegeDeleteRequest\x1a\x18.platformserver.Response\x12G\n\tfindChild\x12 .platformserver.FindChildRequest\x1a\x18.platformserver.Response\x12L\n\x07\x66indAll\x12\'.platformserver.FindAllPrivilegeRequest\x1a\x18.platformserver.Response\x12Y\n\x16\x66indPrivilegeSelective\x12%.platformserver.FindPrivilegesRequest\x1a\x18.platformserver.Response\x12\x43\n\x07\x66indOne\x12\x1e.platformserver.FindOneRequest\x1a\x18.platformserver.ResponseBR\n1com.szwdcloud.platformserver.proto.platformserverB\x1bServerPrivilegeServiceProtoP\x01\x62\x06proto3')
  ,
  dependencies=[ServerCommonMessage__pb2.DESCRIPTOR,])




_PRIVILEGESAVEREQUEST = _descriptor.Descriptor(
  name='PrivilegeSaveRequest',
  full_name='platformserver.PrivilegeSaveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parentId', full_name='platformserver.PrivilegeSaveRequest.parentId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='platformserver.PrivilegeSaveRequest.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='platformserver.PrivilegeSaveRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='systemCategory', full_name='platformserver.PrivilegeSaveRequest.systemCategory', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='platformserver.PrivilegeSaveRequest.type', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='platformserver.PrivilegeSaveRequest.url', index=5,
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
  serialized_start=75,
  serialized_end=194,
)


_PRIVILEGEUPDATEREQUEST = _descriptor.Descriptor(
  name='PrivilegeUpdateRequest',
  full_name='platformserver.PrivilegeUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.PrivilegeUpdateRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentId', full_name='platformserver.PrivilegeUpdateRequest.parentId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='platformserver.PrivilegeUpdateRequest.code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='platformserver.PrivilegeUpdateRequest.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moduleName', full_name='platformserver.PrivilegeUpdateRequest.moduleName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='systemCategory', full_name='platformserver.PrivilegeUpdateRequest.systemCategory', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='platformserver.PrivilegeUpdateRequest.type', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='platformserver.PrivilegeUpdateRequest.url', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=197,
  serialized_end=350,
)


_FINDCHILDREQUEST = _descriptor.Descriptor(
  name='FindChildRequest',
  full_name='platformserver.FindChildRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='systemId', full_name='platformserver.FindChildRequest.systemId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentid', full_name='platformserver.FindChildRequest.parentid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentName', full_name='platformserver.FindChildRequest.parentName', index=2,
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
  serialized_start=352,
  serialized_end=426,
)


_FINDCHILDRESULT_PRIVILEGE = _descriptor.Descriptor(
  name='Privilege',
  full_name='platformserver.FindChildResult.Privilege',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.FindChildResult.Privilege.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='platformserver.FindChildResult.Privilege.name', index=1,
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
  serialized_start=509,
  serialized_end=546,
)

_FINDCHILDRESULT = _descriptor.Descriptor(
  name='FindChildResult',
  full_name='platformserver.FindChildResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='privilege', full_name='platformserver.FindChildResult.privilege', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDCHILDRESULT_PRIVILEGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=546,
)


_PRIVILEGEDELETEREQUEST = _descriptor.Descriptor(
  name='PrivilegeDeleteRequest',
  full_name='platformserver.PrivilegeDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.PrivilegeDeleteRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=548,
  serialized_end=584,
)


_FINDPRIVILEGESREQUEST = _descriptor.Descriptor(
  name='FindPrivilegesRequest',
  full_name='platformserver.FindPrivilegesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='systemId', full_name='platformserver.FindPrivilegesRequest.systemId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='platformserver.FindPrivilegesRequest.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=586,
  serialized_end=641,
)


_FINDPRIVILEGESRESULT_PRIVILEGE = _descriptor.Descriptor(
  name='Privilege',
  full_name='platformserver.FindPrivilegesResult.Privilege',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.FindPrivilegesResult.Privilege.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='platformserver.FindPrivilegesResult.Privilege.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='platformserver.FindPrivilegesResult.Privilege.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='platformserver.FindPrivilegesResult.Privilege.type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='platformserver.FindPrivilegesResult.Privilege.url', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentId', full_name='platformserver.FindPrivilegesResult.Privilege.parentId', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=735,
  serialized_end=831,
)

_FINDPRIVILEGESRESULT = _descriptor.Descriptor(
  name='FindPrivilegesResult',
  full_name='platformserver.FindPrivilegesResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='privilege', full_name='platformserver.FindPrivilegesResult.privilege', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDPRIVILEGESRESULT_PRIVILEGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=644,
  serialized_end=831,
)


_FINDALLPRIVILEGEREQUEST = _descriptor.Descriptor(
  name='FindAllPrivilegeRequest',
  full_name='platformserver.FindAllPrivilegeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='systemId', full_name='platformserver.FindAllPrivilegeRequest.systemId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module', full_name='platformserver.FindAllPrivilegeRequest.module', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='platformserver.FindAllPrivilegeRequest.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageNo', full_name='platformserver.FindAllPrivilegeRequest.pageNo', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='platformserver.FindAllPrivilegeRequest.pageSize', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=833,
  serialized_end=943,
)


_FINDALLPRIVILEGERESULT_PRIVILEGE = _descriptor.Descriptor(
  name='Privilege',
  full_name='platformserver.FindAllPrivilegeResult.Privilege',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.FindAllPrivilegeResult.Privilege.id', index=0,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='platformserver.FindAllPrivilegeResult.Privilege.code', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='platformserver.FindAllPrivilegeResult.Privilege.name', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module', full_name='platformserver.FindAllPrivilegeResult.Privilege.module', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='platformserver.FindAllPrivilegeResult.Privilege.type', index=4,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='platformserver.FindAllPrivilegeResult.Privilege.url', index=5,
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
  serialized_start=1105,
  serialized_end=1199,
)

_FINDALLPRIVILEGERESULT = _descriptor.Descriptor(
  name='FindAllPrivilegeResult',
  full_name='platformserver.FindAllPrivilegeResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='privilege', full_name='platformserver.FindAllPrivilegeResult.privilege', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='platformserver.FindAllPrivilegeResult.total', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pages', full_name='platformserver.FindAllPrivilegeResult.pages', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageNo', full_name='platformserver.FindAllPrivilegeResult.pageNo', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='platformserver.FindAllPrivilegeResult.pageSize', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDALLPRIVILEGERESULT_PRIVILEGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=946,
  serialized_end=1199,
)


_FINDONEREQUEST = _descriptor.Descriptor(
  name='FindOneRequest',
  full_name='platformserver.FindOneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.FindOneRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1201,
  serialized_end=1229,
)


_FINDONERESULT = _descriptor.Descriptor(
  name='FindOneResult',
  full_name='platformserver.FindOneResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.FindOneResult.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='platformserver.FindOneResult.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='platformserver.FindOneResult.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='platformserver.FindOneResult.type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='platformserver.FindOneResult.url', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='systemId', full_name='platformserver.FindOneResult.systemId', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentIds', full_name='platformserver.FindOneResult.parentIds', index=6,
      number=7, type=9, cpp_type=9, label=3,
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
  serialized_start=1231,
  serialized_end=1350,
)

_FINDCHILDRESULT_PRIVILEGE.containing_type = _FINDCHILDRESULT
_FINDCHILDRESULT.fields_by_name['privilege'].message_type = _FINDCHILDRESULT_PRIVILEGE
_FINDPRIVILEGESRESULT_PRIVILEGE.containing_type = _FINDPRIVILEGESRESULT
_FINDPRIVILEGESRESULT.fields_by_name['privilege'].message_type = _FINDPRIVILEGESRESULT_PRIVILEGE
_FINDALLPRIVILEGERESULT_PRIVILEGE.containing_type = _FINDALLPRIVILEGERESULT
_FINDALLPRIVILEGERESULT.fields_by_name['privilege'].message_type = _FINDALLPRIVILEGERESULT_PRIVILEGE
DESCRIPTOR.message_types_by_name['PrivilegeSaveRequest'] = _PRIVILEGESAVEREQUEST
DESCRIPTOR.message_types_by_name['PrivilegeUpdateRequest'] = _PRIVILEGEUPDATEREQUEST
DESCRIPTOR.message_types_by_name['FindChildRequest'] = _FINDCHILDREQUEST
DESCRIPTOR.message_types_by_name['FindChildResult'] = _FINDCHILDRESULT
DESCRIPTOR.message_types_by_name['PrivilegeDeleteRequest'] = _PRIVILEGEDELETEREQUEST
DESCRIPTOR.message_types_by_name['FindPrivilegesRequest'] = _FINDPRIVILEGESREQUEST
DESCRIPTOR.message_types_by_name['FindPrivilegesResult'] = _FINDPRIVILEGESRESULT
DESCRIPTOR.message_types_by_name['FindAllPrivilegeRequest'] = _FINDALLPRIVILEGEREQUEST
DESCRIPTOR.message_types_by_name['FindAllPrivilegeResult'] = _FINDALLPRIVILEGERESULT
DESCRIPTOR.message_types_by_name['FindOneRequest'] = _FINDONEREQUEST
DESCRIPTOR.message_types_by_name['FindOneResult'] = _FINDONERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PrivilegeSaveRequest = _reflection.GeneratedProtocolMessageType('PrivilegeSaveRequest', (_message.Message,), dict(
  DESCRIPTOR = _PRIVILEGESAVEREQUEST,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.PrivilegeSaveRequest)
  ))
_sym_db.RegisterMessage(PrivilegeSaveRequest)

PrivilegeUpdateRequest = _reflection.GeneratedProtocolMessageType('PrivilegeUpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _PRIVILEGEUPDATEREQUEST,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.PrivilegeUpdateRequest)
  ))
_sym_db.RegisterMessage(PrivilegeUpdateRequest)

FindChildRequest = _reflection.GeneratedProtocolMessageType('FindChildRequest', (_message.Message,), dict(
  DESCRIPTOR = _FINDCHILDREQUEST,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.FindChildRequest)
  ))
_sym_db.RegisterMessage(FindChildRequest)

FindChildResult = _reflection.GeneratedProtocolMessageType('FindChildResult', (_message.Message,), dict(

  Privilege = _reflection.GeneratedProtocolMessageType('Privilege', (_message.Message,), dict(
    DESCRIPTOR = _FINDCHILDRESULT_PRIVILEGE,
    __module__ = 'ServerPrivilegeService_pb2'
    # @@protoc_insertion_point(class_scope:platformserver.FindChildResult.Privilege)
    ))
  ,
  DESCRIPTOR = _FINDCHILDRESULT,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.FindChildResult)
  ))
_sym_db.RegisterMessage(FindChildResult)
_sym_db.RegisterMessage(FindChildResult.Privilege)

PrivilegeDeleteRequest = _reflection.GeneratedProtocolMessageType('PrivilegeDeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _PRIVILEGEDELETEREQUEST,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.PrivilegeDeleteRequest)
  ))
_sym_db.RegisterMessage(PrivilegeDeleteRequest)

FindPrivilegesRequest = _reflection.GeneratedProtocolMessageType('FindPrivilegesRequest', (_message.Message,), dict(
  DESCRIPTOR = _FINDPRIVILEGESREQUEST,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.FindPrivilegesRequest)
  ))
_sym_db.RegisterMessage(FindPrivilegesRequest)

FindPrivilegesResult = _reflection.GeneratedProtocolMessageType('FindPrivilegesResult', (_message.Message,), dict(

  Privilege = _reflection.GeneratedProtocolMessageType('Privilege', (_message.Message,), dict(
    DESCRIPTOR = _FINDPRIVILEGESRESULT_PRIVILEGE,
    __module__ = 'ServerPrivilegeService_pb2'
    # @@protoc_insertion_point(class_scope:platformserver.FindPrivilegesResult.Privilege)
    ))
  ,
  DESCRIPTOR = _FINDPRIVILEGESRESULT,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.FindPrivilegesResult)
  ))
_sym_db.RegisterMessage(FindPrivilegesResult)
_sym_db.RegisterMessage(FindPrivilegesResult.Privilege)

FindAllPrivilegeRequest = _reflection.GeneratedProtocolMessageType('FindAllPrivilegeRequest', (_message.Message,), dict(
  DESCRIPTOR = _FINDALLPRIVILEGEREQUEST,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.FindAllPrivilegeRequest)
  ))
_sym_db.RegisterMessage(FindAllPrivilegeRequest)

FindAllPrivilegeResult = _reflection.GeneratedProtocolMessageType('FindAllPrivilegeResult', (_message.Message,), dict(

  Privilege = _reflection.GeneratedProtocolMessageType('Privilege', (_message.Message,), dict(
    DESCRIPTOR = _FINDALLPRIVILEGERESULT_PRIVILEGE,
    __module__ = 'ServerPrivilegeService_pb2'
    # @@protoc_insertion_point(class_scope:platformserver.FindAllPrivilegeResult.Privilege)
    ))
  ,
  DESCRIPTOR = _FINDALLPRIVILEGERESULT,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.FindAllPrivilegeResult)
  ))
_sym_db.RegisterMessage(FindAllPrivilegeResult)
_sym_db.RegisterMessage(FindAllPrivilegeResult.Privilege)

FindOneRequest = _reflection.GeneratedProtocolMessageType('FindOneRequest', (_message.Message,), dict(
  DESCRIPTOR = _FINDONEREQUEST,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.FindOneRequest)
  ))
_sym_db.RegisterMessage(FindOneRequest)

FindOneResult = _reflection.GeneratedProtocolMessageType('FindOneResult', (_message.Message,), dict(
  DESCRIPTOR = _FINDONERESULT,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.FindOneResult)
  ))
_sym_db.RegisterMessage(FindOneResult)


DESCRIPTOR._options = None

_SERVERPRIVILEGESERVICE = _descriptor.ServiceDescriptor(
  name='ServerPrivilegeService',
  full_name='platformserver.ServerPrivilegeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1353,
  serialized_end=1912,
  methods=[
  _descriptor.MethodDescriptor(
    name='save',
    full_name='platformserver.ServerPrivilegeService.save',
    index=0,
    containing_service=None,
    input_type=_PRIVILEGESAVEREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='platformserver.ServerPrivilegeService.update',
    index=1,
    containing_service=None,
    input_type=_PRIVILEGEUPDATEREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='platformserver.ServerPrivilegeService.delete',
    index=2,
    containing_service=None,
    input_type=_PRIVILEGEDELETEREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='findChild',
    full_name='platformserver.ServerPrivilegeService.findChild',
    index=3,
    containing_service=None,
    input_type=_FINDCHILDREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='findAll',
    full_name='platformserver.ServerPrivilegeService.findAll',
    index=4,
    containing_service=None,
    input_type=_FINDALLPRIVILEGEREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='findPrivilegeSelective',
    full_name='platformserver.ServerPrivilegeService.findPrivilegeSelective',
    index=5,
    containing_service=None,
    input_type=_FINDPRIVILEGESREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='findOne',
    full_name='platformserver.ServerPrivilegeService.findOne',
    index=6,
    containing_service=None,
    input_type=_FINDONEREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVERPRIVILEGESERVICE)

DESCRIPTOR.services_by_name['ServerPrivilegeService'] = _SERVERPRIVILEGESERVICE

# @@protoc_insertion_point(module_scope)