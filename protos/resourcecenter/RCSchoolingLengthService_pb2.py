# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RCSchoolingLengthService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import RCCommon_pb2 as RCCommon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='RCSchoolingLengthService.proto',
  package='resourcecenter',
  syntax='proto3',
  serialized_options=_b('\n&com.szwdcloud.resource.schoolinglengthB\035RCSchoolinglengthServiceProtoP\001'),
  serialized_pb=_b('\n\x1eRCSchoolingLengthService.proto\x12\x0eresourcecenter\x1a\x0eRCCommon.proto\"$\n\x16RequestSchoolingLength\x12\n\n\x02id\x18\x01 \x01(\x05\"Y\n\x0fSchoolingLength\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x1b\n\x13schoolingLengthName\x18\x03 \x01(\t\x12\x0f\n\x07gradeId\x18\x04 \x01(\t\"h\n\x1bResponseSchoolingLengthList\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12.\n\x05\x64\x61tas\x18\x03 \x03(\x0b\x32\x1f.resourcecenter.SchoolingLength2\x88\x01\n\x18RCSchoolinglengthService\x12l\n\x13listSchoolingLength\x12&.resourcecenter.RequestSchoolingLength\x1a+.resourcecenter.ResponseSchoolingLengthList\"\x00\x42I\n&com.szwdcloud.resource.schoolinglengthB\x1dRCSchoolinglengthServiceProtoP\x01\x62\x06proto3')
  ,
  dependencies=[RCCommon__pb2.DESCRIPTOR,])




_REQUESTSCHOOLINGLENGTH = _descriptor.Descriptor(
  name='RequestSchoolingLength',
  full_name='resourcecenter.RequestSchoolingLength',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='resourcecenter.RequestSchoolingLength.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=66,
  serialized_end=102,
)


_SCHOOLINGLENGTH = _descriptor.Descriptor(
  name='SchoolingLength',
  full_name='resourcecenter.SchoolingLength',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='resourcecenter.SchoolingLength.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='resourcecenter.SchoolingLength.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolingLengthName', full_name='resourcecenter.SchoolingLength.schoolingLengthName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gradeId', full_name='resourcecenter.SchoolingLength.gradeId', index=3,
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
  serialized_start=104,
  serialized_end=193,
)


_RESPONSESCHOOLINGLENGTHLIST = _descriptor.Descriptor(
  name='ResponseSchoolingLengthList',
  full_name='resourcecenter.ResponseSchoolingLengthList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='resourcecenter.ResponseSchoolingLengthList.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='resourcecenter.ResponseSchoolingLengthList.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datas', full_name='resourcecenter.ResponseSchoolingLengthList.datas', index=2,
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
  serialized_start=195,
  serialized_end=299,
)

_RESPONSESCHOOLINGLENGTHLIST.fields_by_name['datas'].message_type = _SCHOOLINGLENGTH
DESCRIPTOR.message_types_by_name['RequestSchoolingLength'] = _REQUESTSCHOOLINGLENGTH
DESCRIPTOR.message_types_by_name['SchoolingLength'] = _SCHOOLINGLENGTH
DESCRIPTOR.message_types_by_name['ResponseSchoolingLengthList'] = _RESPONSESCHOOLINGLENGTHLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestSchoolingLength = _reflection.GeneratedProtocolMessageType('RequestSchoolingLength', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSCHOOLINGLENGTH,
  __module__ = 'RCSchoolingLengthService_pb2'
  # @@protoc_insertion_point(class_scope:resourcecenter.RequestSchoolingLength)
  ))
_sym_db.RegisterMessage(RequestSchoolingLength)

SchoolingLength = _reflection.GeneratedProtocolMessageType('SchoolingLength', (_message.Message,), dict(
  DESCRIPTOR = _SCHOOLINGLENGTH,
  __module__ = 'RCSchoolingLengthService_pb2'
  # @@protoc_insertion_point(class_scope:resourcecenter.SchoolingLength)
  ))
_sym_db.RegisterMessage(SchoolingLength)

ResponseSchoolingLengthList = _reflection.GeneratedProtocolMessageType('ResponseSchoolingLengthList', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSESCHOOLINGLENGTHLIST,
  __module__ = 'RCSchoolingLengthService_pb2'
  # @@protoc_insertion_point(class_scope:resourcecenter.ResponseSchoolingLengthList)
  ))
_sym_db.RegisterMessage(ResponseSchoolingLengthList)


DESCRIPTOR._options = None

_RCSCHOOLINGLENGTHSERVICE = _descriptor.ServiceDescriptor(
  name='RCSchoolinglengthService',
  full_name='resourcecenter.RCSchoolinglengthService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=302,
  serialized_end=438,
  methods=[
  _descriptor.MethodDescriptor(
    name='listSchoolingLength',
    full_name='resourcecenter.RCSchoolinglengthService.listSchoolingLength',
    index=0,
    containing_service=None,
    input_type=_REQUESTSCHOOLINGLENGTH,
    output_type=_RESPONSESCHOOLINGLENGTHLIST,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RCSCHOOLINGLENGTHSERVICE)

DESCRIPTOR.services_by_name['RCSchoolinglengthService'] = _RCSCHOOLINGLENGTHSERVICE

# @@protoc_insertion_point(module_scope)
