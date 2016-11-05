# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gps.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gps.proto',
  package='gps',
  syntax='proto2',
  serialized_pb=_b('\n\tgps.proto\x12\x03gps\"}\n\x06Sample\x12\x0e\n\x01T\x18\x01 \x01(\r:\x03\x31\x30\x30\x12\n\n\x02\x64X\x18\x02 \x01(\r\x12\n\n\x02\x64U\x18\x03 \x01(\r\x12\n\n\x02\x64O\x18\x04 \x01(\r\x12\r\n\x01X\x18\x05 \x03(\x02\x42\x02\x10\x01\x12\r\n\x01U\x18\x06 \x03(\x02\x42\x02\x10\x01\x12\x0f\n\x03obs\x18\x07 \x03(\x02\x42\x02\x10\x01\x12\x10\n\x04meta\x18\x08 \x03(\x02\x42\x02\x10\x01*\x88\x04\n\nSampleType\x12\n\n\x06\x41\x43TION\x10\x00\x12\x10\n\x0cJOINT_ANGLES\x10\x01\x12\x14\n\x10JOINT_VELOCITIES\x10\x02\x12\x17\n\x13\x45ND_EFFECTOR_POINTS\x10\x03\x12!\n\x1d\x45ND_EFFECTOR_POINT_VELOCITIES\x10\x04\x12 \n\x1c\x45ND_EFFECTOR_POINT_JACOBIANS\x10\x05\x12$\n END_EFFECTOR_POINT_ROT_JACOBIANS\x10\x06\x12\x1a\n\x16\x45ND_EFFECTOR_POSITIONS\x10\x07\x12\x1a\n\x16\x45ND_EFFECTOR_ROTATIONS\x10\x08\x12\x1a\n\x16\x45ND_EFFECTOR_JACOBIANS\x10\t\x12\x19\n\x15\x45ND_EFFECTOR_HESSIANS\x10\n\x12\r\n\tRGB_IMAGE\x10\x0b\x12\x0f\n\x0b\x44\x45PTH_IMAGE\x10\x0c\x12\x12\n\x0eRGB_IMAGE_SIZE\x10\r\x12\x11\n\rCONTEXT_IMAGE\x10\x0e\x12\x16\n\x12\x43ONTEXT_IMAGE_SIZE\x10\x0f\x12\x0e\n\nIMAGE_FEAT\x10\x10\x12!\n\x1d\x45ND_EFFECTOR_POINTS_NO_TARGET\x10\x11\x12+\n\'END_EFFECTOR_POINT_VELOCITIES_NO_TARGET\x10\x12\x12\x14\n\x10TOTAL_DATA_TYPES\x10\x13*J\n\x0c\x41\x63tuatorType\x12\r\n\tTRIAL_ARM\x10\x00\x12\x11\n\rAUXILIARY_ARM\x10\x01\x12\x18\n\x14TOTAL_ACTUATOR_TYPES\x10\x02*_\n\x13PositionControlMode\x12\x0e\n\nNO_CONTROL\x10\x00\x12\x0f\n\x0bJOINT_SPACE\x10\x01\x12\x0e\n\nTASK_SPACE\x10\x02\x12\x17\n\x13TOTAL_CONTROL_MODES\x10\x03*o\n\x0e\x43ontrollerType\x12\x18\n\x14LIN_GAUSS_CONTROLLER\x10\x00\x12\x14\n\x10\x43\x41\x46\x46\x45_CONTROLLER\x10\x01\x12\x11\n\rTF_CONTROLLER\x10\x02\x12\x1a\n\x16TOTAL_CONTROLLER_TYPES\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_SAMPLETYPE = _descriptor.EnumDescriptor(
  name='SampleType',
  full_name='gps.SampleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOINT_ANGLES', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOINT_VELOCITIES', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_EFFECTOR_POINTS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_EFFECTOR_POINT_VELOCITIES', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_EFFECTOR_POINT_JACOBIANS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_EFFECTOR_POINT_ROT_JACOBIANS', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_EFFECTOR_POSITIONS', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_EFFECTOR_ROTATIONS', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_EFFECTOR_JACOBIANS', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_EFFECTOR_HESSIANS', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RGB_IMAGE', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPTH_IMAGE', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RGB_IMAGE_SIZE', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTEXT_IMAGE', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTEXT_IMAGE_SIZE', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_FEAT', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_EFFECTOR_POINTS_NO_TARGET', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_EFFECTOR_POINT_VELOCITIES_NO_TARGET', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOTAL_DATA_TYPES', index=19, number=19,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=146,
  serialized_end=666,
)
_sym_db.RegisterEnumDescriptor(_SAMPLETYPE)

SampleType = enum_type_wrapper.EnumTypeWrapper(_SAMPLETYPE)
_ACTUATORTYPE = _descriptor.EnumDescriptor(
  name='ActuatorType',
  full_name='gps.ActuatorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRIAL_ARM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUXILIARY_ARM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOTAL_ACTUATOR_TYPES', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=668,
  serialized_end=742,
)
_sym_db.RegisterEnumDescriptor(_ACTUATORTYPE)

ActuatorType = enum_type_wrapper.EnumTypeWrapper(_ACTUATORTYPE)
_POSITIONCONTROLMODE = _descriptor.EnumDescriptor(
  name='PositionControlMode',
  full_name='gps.PositionControlMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_CONTROL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOINT_SPACE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_SPACE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOTAL_CONTROL_MODES', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=744,
  serialized_end=839,
)
_sym_db.RegisterEnumDescriptor(_POSITIONCONTROLMODE)

PositionControlMode = enum_type_wrapper.EnumTypeWrapper(_POSITIONCONTROLMODE)
_CONTROLLERTYPE = _descriptor.EnumDescriptor(
  name='ControllerType',
  full_name='gps.ControllerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LIN_GAUSS_CONTROLLER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAFFE_CONTROLLER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TF_CONTROLLER', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOTAL_CONTROLLER_TYPES', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=841,
  serialized_end=952,
)
_sym_db.RegisterEnumDescriptor(_CONTROLLERTYPE)

ControllerType = enum_type_wrapper.EnumTypeWrapper(_CONTROLLERTYPE)
ACTION = 0
JOINT_ANGLES = 1
JOINT_VELOCITIES = 2
END_EFFECTOR_POINTS = 3
END_EFFECTOR_POINT_VELOCITIES = 4
END_EFFECTOR_POINT_JACOBIANS = 5
END_EFFECTOR_POINT_ROT_JACOBIANS = 6
END_EFFECTOR_POSITIONS = 7
END_EFFECTOR_ROTATIONS = 8
END_EFFECTOR_JACOBIANS = 9
END_EFFECTOR_HESSIANS = 10
RGB_IMAGE = 11
DEPTH_IMAGE = 12
RGB_IMAGE_SIZE = 13
CONTEXT_IMAGE = 14
CONTEXT_IMAGE_SIZE = 15
IMAGE_FEAT = 16
END_EFFECTOR_POINTS_NO_TARGET = 17
END_EFFECTOR_POINT_VELOCITIES_NO_TARGET = 18
TOTAL_DATA_TYPES = 19
TRIAL_ARM = 0
AUXILIARY_ARM = 1
TOTAL_ACTUATOR_TYPES = 2
NO_CONTROL = 0
JOINT_SPACE = 1
TASK_SPACE = 2
TOTAL_CONTROL_MODES = 3
LIN_GAUSS_CONTROLLER = 0
CAFFE_CONTROLLER = 1
TF_CONTROLLER = 2
TOTAL_CONTROLLER_TYPES = 3



_SAMPLE = _descriptor.Descriptor(
  name='Sample',
  full_name='gps.Sample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='T', full_name='gps.Sample.T', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dX', full_name='gps.Sample.dX', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dU', full_name='gps.Sample.dU', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dO', full_name='gps.Sample.dO', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='X', full_name='gps.Sample.X', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='U', full_name='gps.Sample.U', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='obs', full_name='gps.Sample.obs', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='meta', full_name='gps.Sample.meta', index=7,
      number=8, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['Sample'] = _SAMPLE
DESCRIPTOR.enum_types_by_name['SampleType'] = _SAMPLETYPE
DESCRIPTOR.enum_types_by_name['ActuatorType'] = _ACTUATORTYPE
DESCRIPTOR.enum_types_by_name['PositionControlMode'] = _POSITIONCONTROLMODE
DESCRIPTOR.enum_types_by_name['ControllerType'] = _CONTROLLERTYPE

Sample = _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLE,
  __module__ = 'gps_pb2'
  # @@protoc_insertion_point(class_scope:gps.Sample)
  ))
_sym_db.RegisterMessage(Sample)


_SAMPLE.fields_by_name['X'].has_options = True
_SAMPLE.fields_by_name['X']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_SAMPLE.fields_by_name['U'].has_options = True
_SAMPLE.fields_by_name['U']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_SAMPLE.fields_by_name['obs'].has_options = True
_SAMPLE.fields_by_name['obs']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_SAMPLE.fields_by_name['meta'].has_options = True
_SAMPLE.fields_by_name['meta']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
