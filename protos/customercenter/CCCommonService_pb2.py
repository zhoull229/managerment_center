# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CCCommonService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='CCCommonService.proto',
  package='customercenter',
  syntax='proto3',
  serialized_options=_b('\n1com.szwdcloud.customercenter.proto.customercenterB\024CCCommonServiceProtoP\001'),
  serialized_pb=_b('\n\x15\x43\x43\x43ommonService.proto\x12\x0e\x63ustomercenter\"@\n\x0e\x41\x64\x64ressListMsg\x12.\n\naddressMsg\x18\x01 \x03(\x0b\x32\x1a.customercenter.AddressMsg\"z\n\nAddressMsg\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nprovinceId\x18\x02 \x01(\t\x12\x14\n\x0cprovinceName\x18\x03 \x01(\t\x12\x0e\n\x06\x63ityId\x18\x04 \x01(\t\x12\x10\n\x08\x63ityName\x18\x05 \x01(\t\x12\x14\n\x0c\x64istrictName\x18\x06 \x01(\t\"#\n\x13RequestListProvince\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"%\n\x0fRequestListCity\x12\x12\n\nprovinceId\x18\x01 \x01(\t\"%\n\x13RequestListDistrict\x12\x0e\n\x06\x63ityId\x18\x01 \x01(\t2\x0f\n\rCommonServiceBK\n1com.szwdcloud.customercenter.proto.customercenterB\x14\x43\x43\x43ommonServiceProtoP\x01\x62\x06proto3')
)




_ADDRESSLISTMSG = _descriptor.Descriptor(
  name='AddressListMsg',
  full_name='customercenter.AddressListMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addressMsg', full_name='customercenter.AddressListMsg.addressMsg', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=41,
  serialized_end=105,
)


_ADDRESSMSG = _descriptor.Descriptor(
  name='AddressMsg',
  full_name='customercenter.AddressMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='customercenter.AddressMsg.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provinceId', full_name='customercenter.AddressMsg.provinceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provinceName', full_name='customercenter.AddressMsg.provinceName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cityId', full_name='customercenter.AddressMsg.cityId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cityName', full_name='customercenter.AddressMsg.cityName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='districtName', full_name='customercenter.AddressMsg.districtName', index=5,
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
  serialized_start=107,
  serialized_end=229,
)


_REQUESTLISTPROVINCE = _descriptor.Descriptor(
  name='RequestListProvince',
  full_name='customercenter.RequestListProvince',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='customercenter.RequestListProvince.code', index=0,
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
  serialized_start=231,
  serialized_end=266,
)


_REQUESTLISTCITY = _descriptor.Descriptor(
  name='RequestListCity',
  full_name='customercenter.RequestListCity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provinceId', full_name='customercenter.RequestListCity.provinceId', index=0,
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
  serialized_start=268,
  serialized_end=305,
)


_REQUESTLISTDISTRICT = _descriptor.Descriptor(
  name='RequestListDistrict',
  full_name='customercenter.RequestListDistrict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cityId', full_name='customercenter.RequestListDistrict.cityId', index=0,
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
  serialized_start=307,
  serialized_end=344,
)

_ADDRESSLISTMSG.fields_by_name['addressMsg'].message_type = _ADDRESSMSG
DESCRIPTOR.message_types_by_name['AddressListMsg'] = _ADDRESSLISTMSG
DESCRIPTOR.message_types_by_name['AddressMsg'] = _ADDRESSMSG
DESCRIPTOR.message_types_by_name['RequestListProvince'] = _REQUESTLISTPROVINCE
DESCRIPTOR.message_types_by_name['RequestListCity'] = _REQUESTLISTCITY
DESCRIPTOR.message_types_by_name['RequestListDistrict'] = _REQUESTLISTDISTRICT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddressListMsg = _reflection.GeneratedProtocolMessageType('AddressListMsg', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSLISTMSG,
  __module__ = 'CCCommonService_pb2'
  # @@protoc_insertion_point(class_scope:customercenter.AddressListMsg)
  ))
_sym_db.RegisterMessage(AddressListMsg)

AddressMsg = _reflection.GeneratedProtocolMessageType('AddressMsg', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSMSG,
  __module__ = 'CCCommonService_pb2'
  # @@protoc_insertion_point(class_scope:customercenter.AddressMsg)
  ))
_sym_db.RegisterMessage(AddressMsg)

RequestListProvince = _reflection.GeneratedProtocolMessageType('RequestListProvince', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTLISTPROVINCE,
  __module__ = 'CCCommonService_pb2'
  # @@protoc_insertion_point(class_scope:customercenter.RequestListProvince)
  ))
_sym_db.RegisterMessage(RequestListProvince)

RequestListCity = _reflection.GeneratedProtocolMessageType('RequestListCity', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTLISTCITY,
  __module__ = 'CCCommonService_pb2'
  # @@protoc_insertion_point(class_scope:customercenter.RequestListCity)
  ))
_sym_db.RegisterMessage(RequestListCity)

RequestListDistrict = _reflection.GeneratedProtocolMessageType('RequestListDistrict', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTLISTDISTRICT,
  __module__ = 'CCCommonService_pb2'
  # @@protoc_insertion_point(class_scope:customercenter.RequestListDistrict)
  ))
_sym_db.RegisterMessage(RequestListDistrict)


DESCRIPTOR._options = None

_COMMONSERVICE = _descriptor.ServiceDescriptor(
  name='CommonService',
  full_name='customercenter.CommonService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=346,
  serialized_end=361,
  methods=[
])
_sym_db.RegisterServiceDescriptor(_COMMONSERVICE)

DESCRIPTOR.services_by_name['CommonService'] = _COMMONSERVICE

# @@protoc_insertion_point(module_scope)
