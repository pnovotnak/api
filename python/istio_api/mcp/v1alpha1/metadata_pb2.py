# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mcp/v1alpha1/metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mcp/v1alpha1/metadata.proto',
  package='istio.mcp.v1alpha1',
  syntax='proto3',
  serialized_options=_b('Z\031istio.io/api/mcp/v1alpha1\250\342\036\001'),
  serialized_pb=_b('\n\x1bmcp/v1alpha1/metadata.proto\x12\x12istio.mcp.v1alpha1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xbb\x02\n\x08Metadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x38\n\x06labels\x18\x04 \x03(\x0b\x32(.istio.mcp.v1alpha1.Metadata.LabelsEntry\x12\x42\n\x0b\x61nnotations\x18\x05 \x03(\x0b\x32-.istio.mcp.v1alpha1.Metadata.AnnotationsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x1fZ\x19istio.io/api/mcp/v1alpha1\xa8\xe2\x1e\x01\x62\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_METADATA_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='istio.mcp.v1alpha1.Metadata.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.mcp.v1alpha1.Metadata.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.mcp.v1alpha1.Metadata.LabelsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=400,
)

_METADATA_ANNOTATIONSENTRY = _descriptor.Descriptor(
  name='AnnotationsEntry',
  full_name='istio.mcp.v1alpha1.Metadata.AnnotationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.mcp.v1alpha1.Metadata.AnnotationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.mcp.v1alpha1.Metadata.AnnotationsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=452,
)

_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='istio.mcp.v1alpha1.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='istio.mcp.v1alpha1.Metadata.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='istio.mcp.v1alpha1.Metadata.create_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='istio.mcp.v1alpha1.Metadata.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='istio.mcp.v1alpha1.Metadata.labels', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='istio.mcp.v1alpha1.Metadata.annotations', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_METADATA_LABELSENTRY, _METADATA_ANNOTATIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=452,
)

_METADATA_LABELSENTRY.containing_type = _METADATA
_METADATA_ANNOTATIONSENTRY.containing_type = _METADATA
_METADATA.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_METADATA.fields_by_name['labels'].message_type = _METADATA_LABELSENTRY
_METADATA.fields_by_name['annotations'].message_type = _METADATA_ANNOTATIONSENTRY
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _METADATA_LABELSENTRY,
    '__module__' : 'mcp.v1alpha1.metadata_pb2'
    # @@protoc_insertion_point(class_scope:istio.mcp.v1alpha1.Metadata.LabelsEntry)
    })
  ,

  'AnnotationsEntry' : _reflection.GeneratedProtocolMessageType('AnnotationsEntry', (_message.Message,), {
    'DESCRIPTOR' : _METADATA_ANNOTATIONSENTRY,
    '__module__' : 'mcp.v1alpha1.metadata_pb2'
    # @@protoc_insertion_point(class_scope:istio.mcp.v1alpha1.Metadata.AnnotationsEntry)
    })
  ,
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'mcp.v1alpha1.metadata_pb2'
  # @@protoc_insertion_point(class_scope:istio.mcp.v1alpha1.Metadata)
  })
_sym_db.RegisterMessage(Metadata)
_sym_db.RegisterMessage(Metadata.LabelsEntry)
_sym_db.RegisterMessage(Metadata.AnnotationsEntry)


DESCRIPTOR._options = None
_METADATA_LABELSENTRY._options = None
_METADATA_ANNOTATIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
