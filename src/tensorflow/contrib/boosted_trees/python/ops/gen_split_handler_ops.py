"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
"""

import collections as _collections

from tensorflow.core.framework import op_def_pb2 as _op_def_pb2

# Needed to trigger the call to _set_call_cpp_shape_fn.
from tensorflow.python.framework import common_shapes as _common_shapes

from tensorflow.python.framework import op_def_registry as _op_def_registry
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import op_def_library as _op_def_library

_build_categorical_equality_splits_outputs = ["output_partition_ids", "gains",
                                             "split_infos"]
_BuildCategoricalEqualitySplitsOutput = _collections.namedtuple(
    "BuildCategoricalEqualitySplits",
    _build_categorical_equality_splits_outputs)


def build_categorical_equality_splits(num_minibatches, partition_ids,
                                      feature_ids, gradients, hessians,
                                      class_id, feature_column_group_id,
                                      bias_feature_id, l1_regularization,
                                      l2_regularization,
                                      tree_complexity_regularization,
                                      min_node_weight, multiclass_strategy,
                                      name=None):
  r"""Find the split that has the best gain for the accumulated stats.

  Args:
    num_minibatches: A `Tensor` of type `int64`.
      A scalar, the number of times per example gradients & hessians
      were accumulated. The stats are divided by this to get per example stats.
    partition_ids: A `Tensor` of type `int32`.
      A rank 1 tensor of partition IDs.
    feature_ids: A `Tensor` of type `int64`. A rank 1 tensor of feature IDs.
    gradients: A `Tensor` of type `float32`. A rank 1 tensor of gradients.
    hessians: A `Tensor` of type `float32`. A rank 1 tensor of hessians.
    class_id: A `Tensor` of type `int32`.
    feature_column_group_id: An `int`.
    bias_feature_id: An `int`.
    l1_regularization: A `float`.
    l2_regularization: A `float`.
    tree_complexity_regularization: A `float`.
    min_node_weight: A `float`.
    multiclass_strategy: An `int`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_partition_ids, gains, split_infos).

    output_partition_ids: A `Tensor` of type `int32`. A rank 1 tensor, the partition IDs that we created splits
      for.
    gains: A `Tensor` of type `float32`. A rank 1 tensor, for the computed gain for the created splits.
    split_infos: A `Tensor` of type `string`. A rank 1 tensor of serialized protos which contains the
      `SplitInfo`s.
  """
  result = _op_def_lib.apply_op("BuildCategoricalEqualitySplits",
                                num_minibatches=num_minibatches,
                                partition_ids=partition_ids,
                                feature_ids=feature_ids, gradients=gradients,
                                hessians=hessians, class_id=class_id,
                                feature_column_group_id=feature_column_group_id,
                                bias_feature_id=bias_feature_id,
                                l1_regularization=l1_regularization,
                                l2_regularization=l2_regularization,
                                tree_complexity_regularization=tree_complexity_regularization,
                                min_node_weight=min_node_weight,
                                multiclass_strategy=multiclass_strategy,
                                name=name)
  return _BuildCategoricalEqualitySplitsOutput._make(result)


_ops.RegisterShape("BuildCategoricalEqualitySplits")(None)

_build_dense_inequality_splits_outputs = ["output_partition_ids", "gains",
                                         "split_infos"]
_BuildDenseInequalitySplitsOutput = _collections.namedtuple(
    "BuildDenseInequalitySplits", _build_dense_inequality_splits_outputs)


def build_dense_inequality_splits(num_minibatches, partition_ids, bucket_ids,
                                  gradients, hessians, bucket_boundaries,
                                  class_id, feature_column_group_id,
                                  l1_regularization, l2_regularization,
                                  tree_complexity_regularization,
                                  min_node_weight, multiclass_strategy,
                                  name=None):
  r"""Find the split that has the best gain for the accumulated stats.

  Args:
    num_minibatches: A `Tensor` of type `int64`.
      A scalar, the number of times per example gradients & hessians
      were accumulated. The stats are divided by this to get per example stats.
    partition_ids: A `Tensor` of type `int32`.
      A rank 1 tensor of partition IDs.
    bucket_ids: A `Tensor` of type `int64`. A rank 1 tensor of buckets IDs.
    gradients: A `Tensor` of type `float32`. A rank 1 tensor of gradients.
    hessians: A `Tensor` of type `float32`. A rank 1 tensor of hessians.
    bucket_boundaries: A `Tensor` of type `float32`.
      A rank 1 tensor, thresholds that were used for bucketization.
    class_id: A `Tensor` of type `int32`.
    feature_column_group_id: An `int`.
    l1_regularization: A `float`.
    l2_regularization: A `float`.
    tree_complexity_regularization: A `float`.
    min_node_weight: A `float`.
    multiclass_strategy: An `int`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_partition_ids, gains, split_infos).

    output_partition_ids: A `Tensor` of type `int32`. A rank 1 tensor, the partition IDs that we created splits
      for.
    gains: A `Tensor` of type `float32`. A rank 1 tensor, for the computed gain for the created splits.
    split_infos: A `Tensor` of type `string`. A rank 1 tensor of serialized protos which contains the
      `SplitInfo`s.
  """
  result = _op_def_lib.apply_op("BuildDenseInequalitySplits",
                                num_minibatches=num_minibatches,
                                partition_ids=partition_ids,
                                bucket_ids=bucket_ids, gradients=gradients,
                                hessians=hessians,
                                bucket_boundaries=bucket_boundaries,
                                class_id=class_id,
                                feature_column_group_id=feature_column_group_id,
                                l1_regularization=l1_regularization,
                                l2_regularization=l2_regularization,
                                tree_complexity_regularization=tree_complexity_regularization,
                                min_node_weight=min_node_weight,
                                multiclass_strategy=multiclass_strategy,
                                name=name)
  return _BuildDenseInequalitySplitsOutput._make(result)


_ops.RegisterShape("BuildDenseInequalitySplits")(None)

_build_sparse_inequality_splits_outputs = ["output_partition_ids", "gains",
                                          "split_infos"]
_BuildSparseInequalitySplitsOutput = _collections.namedtuple(
    "BuildSparseInequalitySplits", _build_sparse_inequality_splits_outputs)


def build_sparse_inequality_splits(num_minibatches, partition_ids, bucket_ids,
                                   gradients, hessians, bucket_boundaries,
                                   class_id, feature_column_group_id,
                                   bias_feature_id, l1_regularization,
                                   l2_regularization,
                                   tree_complexity_regularization,
                                   min_node_weight, multiclass_strategy,
                                   name=None):
  r"""Find the split that has the best gain for the accumulated stats.

  Args:
    num_minibatches: A `Tensor` of type `int64`.
      A scalar, the number of times per example gradients & hessians
      were accumulated. The stats are divided by this to get per example stats.
    partition_ids: A `Tensor` of type `int32`.
      A rank 1 tensor of partition IDs.
    bucket_ids: A `Tensor` of type `int64`. A rank 1 tensor of buckets IDs.
    gradients: A `Tensor` of type `float32`. A rank 1 tensor of gradients.
    hessians: A `Tensor` of type `float32`. A rank 1 tensor of hessians.
    bucket_boundaries: A `Tensor` of type `float32`.
      A rank 1 tensor, thresholds that were used for bucketization.
    class_id: A `Tensor` of type `int32`.
    feature_column_group_id: An `int`.
    bias_feature_id: An `int`.
    l1_regularization: A `float`.
    l2_regularization: A `float`.
    tree_complexity_regularization: A `float`.
    min_node_weight: A `float`.
    multiclass_strategy: An `int`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_partition_ids, gains, split_infos).

    output_partition_ids: A `Tensor` of type `int32`. A rank 1 tensor, the partition IDs that we created splits
      for.
    gains: A `Tensor` of type `float32`. A rank 1 tensor, for the computed gain for the created splits.
    split_infos: A `Tensor` of type `string`. A rank 1 tensor of serialized protos which contains the
      `SplitInfo`s.
  """
  result = _op_def_lib.apply_op("BuildSparseInequalitySplits",
                                num_minibatches=num_minibatches,
                                partition_ids=partition_ids,
                                bucket_ids=bucket_ids, gradients=gradients,
                                hessians=hessians,
                                bucket_boundaries=bucket_boundaries,
                                class_id=class_id,
                                feature_column_group_id=feature_column_group_id,
                                bias_feature_id=bias_feature_id,
                                l1_regularization=l1_regularization,
                                l2_regularization=l2_regularization,
                                tree_complexity_regularization=tree_complexity_regularization,
                                min_node_weight=min_node_weight,
                                multiclass_strategy=multiclass_strategy,
                                name=name)
  return _BuildSparseInequalitySplitsOutput._make(result)


_ops.RegisterShape("BuildSparseInequalitySplits")(None)
def _InitOpDefLibrary(op_list_proto_bytes):
  op_list = _op_def_pb2.OpList()
  op_list.ParseFromString(op_list_proto_bytes)
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_def_lib.add_op_list(op_list)
  return op_def_lib


# op {
#   name: "BuildCategoricalEqualitySplits"
#   input_arg {
#     name: "num_minibatches"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "partition_ids"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "feature_ids"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "gradients"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "hessians"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "class_id"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "output_partition_ids"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "gains"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "split_infos"
#     type: DT_STRING
#   }
#   attr {
#     name: "feature_column_group_id"
#     type: "int"
#   }
#   attr {
#     name: "bias_feature_id"
#     type: "int"
#   }
#   attr {
#     name: "l1_regularization"
#     type: "float"
#   }
#   attr {
#     name: "l2_regularization"
#     type: "float"
#   }
#   attr {
#     name: "tree_complexity_regularization"
#     type: "float"
#   }
#   attr {
#     name: "min_node_weight"
#     type: "float"
#   }
#   attr {
#     name: "multiclass_strategy"
#     type: "int"
#   }
# }
# op {
#   name: "BuildDenseInequalitySplits"
#   input_arg {
#     name: "num_minibatches"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "partition_ids"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "bucket_ids"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "gradients"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "hessians"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "bucket_boundaries"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "class_id"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "output_partition_ids"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "gains"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "split_infos"
#     type: DT_STRING
#   }
#   attr {
#     name: "feature_column_group_id"
#     type: "int"
#   }
#   attr {
#     name: "l1_regularization"
#     type: "float"
#   }
#   attr {
#     name: "l2_regularization"
#     type: "float"
#   }
#   attr {
#     name: "tree_complexity_regularization"
#     type: "float"
#   }
#   attr {
#     name: "min_node_weight"
#     type: "float"
#   }
#   attr {
#     name: "multiclass_strategy"
#     type: "int"
#   }
# }
# op {
#   name: "BuildSparseInequalitySplits"
#   input_arg {
#     name: "num_minibatches"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "partition_ids"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "bucket_ids"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "gradients"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "hessians"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "bucket_boundaries"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "class_id"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "output_partition_ids"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "gains"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "split_infos"
#     type: DT_STRING
#   }
#   attr {
#     name: "feature_column_group_id"
#     type: "int"
#   }
#   attr {
#     name: "bias_feature_id"
#     type: "int"
#   }
#   attr {
#     name: "l1_regularization"
#     type: "float"
#   }
#   attr {
#     name: "l2_regularization"
#     type: "float"
#   }
#   attr {
#     name: "tree_complexity_regularization"
#     type: "float"
#   }
#   attr {
#     name: "min_node_weight"
#     type: "float"
#   }
#   attr {
#     name: "multiclass_strategy"
#     type: "int"
#   }
# }
_op_def_lib = _InitOpDefLibrary(b"\n\211\003\n\036BuildCategoricalEqualitySplits\022\023\n\017num_minibatches\030\t\022\021\n\rpartition_ids\030\003\022\017\n\013feature_ids\030\t\022\r\n\tgradients\030\001\022\014\n\010hessians\030\001\022\014\n\010class_id\030\003\032\030\n\024output_partition_ids\030\003\032\t\n\005gains\030\001\032\017\n\013split_infos\030\007\"\036\n\027feature_column_group_id\022\003int\"\026\n\017bias_feature_id\022\003int\"\032\n\021l1_regularization\022\005float\"\032\n\021l2_regularization\022\005float\"\'\n\036tree_complexity_regularization\022\005float\"\030\n\017min_node_weight\022\005float\"\032\n\023multiclass_strategy\022\003int\n\203\003\n\032BuildDenseInequalitySplits\022\023\n\017num_minibatches\030\t\022\021\n\rpartition_ids\030\003\022\016\n\nbucket_ids\030\t\022\r\n\tgradients\030\001\022\014\n\010hessians\030\001\022\025\n\021bucket_boundaries\030\001\022\014\n\010class_id\030\003\032\030\n\024output_partition_ids\030\003\032\t\n\005gains\030\001\032\017\n\013split_infos\030\007\"\036\n\027feature_column_group_id\022\003int\"\032\n\021l1_regularization\022\005float\"\032\n\021l2_regularization\022\005float\"\'\n\036tree_complexity_regularization\022\005float\"\030\n\017min_node_weight\022\005float\"\032\n\023multiclass_strategy\022\003int\n\234\003\n\033BuildSparseInequalitySplits\022\023\n\017num_minibatches\030\t\022\021\n\rpartition_ids\030\003\022\016\n\nbucket_ids\030\t\022\r\n\tgradients\030\001\022\014\n\010hessians\030\001\022\025\n\021bucket_boundaries\030\001\022\014\n\010class_id\030\003\032\030\n\024output_partition_ids\030\003\032\t\n\005gains\030\001\032\017\n\013split_infos\030\007\"\036\n\027feature_column_group_id\022\003int\"\026\n\017bias_feature_id\022\003int\"\032\n\021l1_regularization\022\005float\"\032\n\021l2_regularization\022\005float\"\'\n\036tree_complexity_regularization\022\005float\"\030\n\017min_node_weight\022\005float\"\032\n\023multiclass_strategy\022\003int")
