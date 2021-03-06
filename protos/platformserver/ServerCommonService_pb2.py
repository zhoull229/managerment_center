# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ServerCommonService.proto

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
  name='ServerCommonService.proto',
  package='platformserver',
  syntax='proto3',
  serialized_options=_b('\n1com.szwdcloud.platformserver.proto.platformserverB\030ServerCommonServiceProtoP\001'),
  serialized_pb=_b('\n\x19ServerCommonService.proto\x12\x0eplatformserver\x1a\x19ServerCommonMessage.proto\"g\n\x0cLoginRequest\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\x12\x11\n\tloginType\x18\x04 \x01(\x05\x12\x13\n\x0bloginSource\x18\x05 \x01(\x05\"\xbc\x01\n\x0bLoginResult\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08userName\x18\x02 \x01(\t\x12\x10\n\x08schoolId\x18\x03 \x01(\x03\x12.\n\x04\x61uth\x18\x04 \x03(\x0b\x32 .platformserver.LoginResult.Auth\x1aM\n\x04\x41uth\x12\n\n\x02id\x18\x05 \x01(\t\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x10\n\x08parentId\x18\x04 \x01(\t2V\n\x13ServerCommonService\x12?\n\x05login\x12\x1c.platformserver.LoginRequest\x1a\x18.platformserver.ResponseBO\n1com.szwdcloud.platformserver.proto.platformserverB\x18ServerCommonServiceProtoP\x01\x62\x06proto3')
  ,
  dependencies=[ServerCommonMessage__pb2.DESCRIPTOR,])




_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='platformserver.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='platformserver.LoginRequest.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='platformserver.LoginRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='platformserver.LoginRequest.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loginType', full_name='platformserver.LoginRequest.loginType', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loginSource', full_name='platformserver.LoginRequest.loginSource', index=4,
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
  serialized_start=72,
  serialized_end=175,
)


_LOGINRESULT_AUTH = _descriptor.Descriptor(
  name='Auth',
  full_name='platformserver.LoginResult.Auth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.LoginResult.Auth.id', index=0,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='platformserver.LoginResult.Auth.code', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='platformserver.LoginResult.Auth.name', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='platformserver.LoginResult.Auth.url', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentId', full_name='platformserver.LoginResult.Auth.parentId', index=4,
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
  serialized_start=289,
  serialized_end=366,
)

_LOGINRESULT = _descriptor.Descriptor(
  name='LoginResult',
  full_name='platformserver.LoginResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.LoginResult.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userName', full_name='platformserver.LoginResult.userName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolId', full_name='platformserver.LoginResult.schoolId', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth', full_name='platformserver.LoginResult.auth', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOGINRESULT_AUTH, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=178,
  serialized_end=366,
)

_LOGINRESULT_AUTH.containing_type = _LOGINRESULT
_LOGINRESULT.fields_by_name['auth'].message_type = _LOGINRESULT_AUTH
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LoginResult'] = _LOGINRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOGINREQUEST,
  __module__ = 'ServerCommonService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.LoginRequest)
  ))
_sym_db.RegisterMessage(LoginRequest)

LoginResult = _reflection.GeneratedProtocolMessageType('LoginResult', (_message.Message,), dict(

  Auth = _reflection.GeneratedProtocolMessageType('Auth', (_message.Message,), dict(
    DESCRIPTOR = _LOGINRESULT_AUTH,
    __module__ = 'ServerCommonService_pb2'
    # @@protoc_insertion_point(class_scope:platformserver.LoginResult.Auth)
    ))
  ,
  DESCRIPTOR = _LOGINRESULT,
  __module__ = 'ServerCommonService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.LoginResult)
  ))
_sym_db.RegisterMessage(LoginResult)
_sym_db.RegisterMessage(LoginResult.Auth)


DESCRIPTOR._options = None

_SERVERCOMMONSERVICE = _descriptor.ServiceDescriptor(
  name='ServerCommonService',
  full_name='platformserver.ServerCommonService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=368,
  serialized_end=454,
  methods=[
  _descriptor.MethodDescriptor(
    name='login',
    full_name='platformserver.ServerCommonService.login',
    index=0,
    containing_service=None,
    input_type=_LOGINREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVERCOMMONSERVICE)

DESCRIPTOR.services_by_name['ServerCommonService'] = _SERVERCOMMONSERVICE

# @@protoc_insertion_point(module_scope)
