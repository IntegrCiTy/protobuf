# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ict/protobuf/obnl.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ict/protobuf/obnl.proto',
  package='obnl.common',
  syntax='proto3',
  serialized_pb=_b('\n\x17ict/protobuf/obnl.proto\x12\x0bobnl.common\"\x0c\n\nSystemInit\"\x15\n\x13SimulatorConnection\"\xb2\x02\n\x13SchedulerConnection\x12\x12\n\nsimulation\x18\x01 \x01(\t\x12K\n\x0einitial_values\x18\x02 \x03(\x0b\x32\x33.obnl.common.SchedulerConnection.InitialValuesEntry\x12M\n\x0f\x61ttribute_links\x18\x03 \x03(\x0b\x32\x34.obnl.common.SchedulerConnection.AttributeLinksEntry\x1a\x34\n\x12InitialValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a\x35\n\x13\x41ttributeLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\\\n\x10\x41ttributeMessage\x12\x17\n\x0fsimulation_time\x18\x01 \x01(\x02\x12\x16\n\x0e\x61ttribute_name\x18\x02 \x01(\t\x12\x17\n\x0f\x61ttribute_value\x18\x03 \x01(\x02\"3\n\x08NextStep\x12\x11\n\ttime_step\x18\x01 \x01(\x02\x12\x14\n\x0c\x63urrent_time\x18\x02 \x01(\x02\"\x06\n\x04Quitb\x06proto3')
)




_SYSTEMINIT = _descriptor.Descriptor(
  name='SystemInit',
  full_name='obnl.common.SystemInit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=52,
)


_SIMULATORCONNECTION = _descriptor.Descriptor(
  name='SimulatorConnection',
  full_name='obnl.common.SimulatorConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=75,
)


_SCHEDULERCONNECTION_INITIALVALUESENTRY = _descriptor.Descriptor(
  name='InitialValuesEntry',
  full_name='obnl.common.SchedulerConnection.InitialValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='obnl.common.SchedulerConnection.InitialValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='obnl.common.SchedulerConnection.InitialValuesEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=329,
)

_SCHEDULERCONNECTION_ATTRIBUTELINKSENTRY = _descriptor.Descriptor(
  name='AttributeLinksEntry',
  full_name='obnl.common.SchedulerConnection.AttributeLinksEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='obnl.common.SchedulerConnection.AttributeLinksEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='obnl.common.SchedulerConnection.AttributeLinksEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=384,
)

_SCHEDULERCONNECTION = _descriptor.Descriptor(
  name='SchedulerConnection',
  full_name='obnl.common.SchedulerConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simulation', full_name='obnl.common.SchedulerConnection.simulation', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initial_values', full_name='obnl.common.SchedulerConnection.initial_values', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute_links', full_name='obnl.common.SchedulerConnection.attribute_links', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SCHEDULERCONNECTION_INITIALVALUESENTRY, _SCHEDULERCONNECTION_ATTRIBUTELINKSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=384,
)


_ATTRIBUTEMESSAGE = _descriptor.Descriptor(
  name='AttributeMessage',
  full_name='obnl.common.AttributeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simulation_time', full_name='obnl.common.AttributeMessage.simulation_time', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute_name', full_name='obnl.common.AttributeMessage.attribute_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute_value', full_name='obnl.common.AttributeMessage.attribute_value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=386,
  serialized_end=478,
)


_NEXTSTEP = _descriptor.Descriptor(
  name='NextStep',
  full_name='obnl.common.NextStep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_step', full_name='obnl.common.NextStep.time_step', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_time', full_name='obnl.common.NextStep.current_time', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=480,
  serialized_end=531,
)


_QUIT = _descriptor.Descriptor(
  name='Quit',
  full_name='obnl.common.Quit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=533,
  serialized_end=539,
)

_SCHEDULERCONNECTION_INITIALVALUESENTRY.containing_type = _SCHEDULERCONNECTION
_SCHEDULERCONNECTION_ATTRIBUTELINKSENTRY.containing_type = _SCHEDULERCONNECTION
_SCHEDULERCONNECTION.fields_by_name['initial_values'].message_type = _SCHEDULERCONNECTION_INITIALVALUESENTRY
_SCHEDULERCONNECTION.fields_by_name['attribute_links'].message_type = _SCHEDULERCONNECTION_ATTRIBUTELINKSENTRY
DESCRIPTOR.message_types_by_name['SystemInit'] = _SYSTEMINIT
DESCRIPTOR.message_types_by_name['SimulatorConnection'] = _SIMULATORCONNECTION
DESCRIPTOR.message_types_by_name['SchedulerConnection'] = _SCHEDULERCONNECTION
DESCRIPTOR.message_types_by_name['AttributeMessage'] = _ATTRIBUTEMESSAGE
DESCRIPTOR.message_types_by_name['NextStep'] = _NEXTSTEP
DESCRIPTOR.message_types_by_name['Quit'] = _QUIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SystemInit = _reflection.GeneratedProtocolMessageType('SystemInit', (_message.Message,), dict(
  DESCRIPTOR = _SYSTEMINIT,
  __module__ = 'ict.protobuf.obnl_pb2'
  # @@protoc_insertion_point(class_scope:obnl.common.SystemInit)
  ))
_sym_db.RegisterMessage(SystemInit)

SimulatorConnection = _reflection.GeneratedProtocolMessageType('SimulatorConnection', (_message.Message,), dict(
  DESCRIPTOR = _SIMULATORCONNECTION,
  __module__ = 'ict.protobuf.obnl_pb2'
  # @@protoc_insertion_point(class_scope:obnl.common.SimulatorConnection)
  ))
_sym_db.RegisterMessage(SimulatorConnection)

SchedulerConnection = _reflection.GeneratedProtocolMessageType('SchedulerConnection', (_message.Message,), dict(

  InitialValuesEntry = _reflection.GeneratedProtocolMessageType('InitialValuesEntry', (_message.Message,), dict(
    DESCRIPTOR = _SCHEDULERCONNECTION_INITIALVALUESENTRY,
    __module__ = 'ict.protobuf.obnl_pb2'
    # @@protoc_insertion_point(class_scope:obnl.common.SchedulerConnection.InitialValuesEntry)
    ))
  ,

  AttributeLinksEntry = _reflection.GeneratedProtocolMessageType('AttributeLinksEntry', (_message.Message,), dict(
    DESCRIPTOR = _SCHEDULERCONNECTION_ATTRIBUTELINKSENTRY,
    __module__ = 'ict.protobuf.obnl_pb2'
    # @@protoc_insertion_point(class_scope:obnl.common.SchedulerConnection.AttributeLinksEntry)
    ))
  ,
  DESCRIPTOR = _SCHEDULERCONNECTION,
  __module__ = 'ict.protobuf.obnl_pb2'
  # @@protoc_insertion_point(class_scope:obnl.common.SchedulerConnection)
  ))
_sym_db.RegisterMessage(SchedulerConnection)
_sym_db.RegisterMessage(SchedulerConnection.InitialValuesEntry)
_sym_db.RegisterMessage(SchedulerConnection.AttributeLinksEntry)

AttributeMessage = _reflection.GeneratedProtocolMessageType('AttributeMessage', (_message.Message,), dict(
  DESCRIPTOR = _ATTRIBUTEMESSAGE,
  __module__ = 'ict.protobuf.obnl_pb2'
  # @@protoc_insertion_point(class_scope:obnl.common.AttributeMessage)
  ))
_sym_db.RegisterMessage(AttributeMessage)

NextStep = _reflection.GeneratedProtocolMessageType('NextStep', (_message.Message,), dict(
  DESCRIPTOR = _NEXTSTEP,
  __module__ = 'ict.protobuf.obnl_pb2'
  # @@protoc_insertion_point(class_scope:obnl.common.NextStep)
  ))
_sym_db.RegisterMessage(NextStep)

Quit = _reflection.GeneratedProtocolMessageType('Quit', (_message.Message,), dict(
  DESCRIPTOR = _QUIT,
  __module__ = 'ict.protobuf.obnl_pb2'
  # @@protoc_insertion_point(class_scope:obnl.common.Quit)
  ))
_sym_db.RegisterMessage(Quit)


_SCHEDULERCONNECTION_INITIALVALUESENTRY.has_options = True
_SCHEDULERCONNECTION_INITIALVALUESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_SCHEDULERCONNECTION_ATTRIBUTELINKSENTRY.has_options = True
_SCHEDULERCONNECTION_ATTRIBUTELINKSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
