# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import RCCommon_pb2 as RCCommon__pb2
import RCPointService_pb2 as RCPointService__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


class RCPointServiceStub(object):
  """定义服务
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.listPointsBySubjectId = channel.unary_unary(
        '/resourcecenter.RCPointService/listPointsBySubjectId',
        request_serializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.SerializeToString,
        response_deserializer=RCCommon__pb2.ListResp.FromString,
        )
    self.listPointsJsonBySubjectId = channel.unary_unary(
        '/resourcecenter.RCPointService/listPointsJsonBySubjectId',
        request_serializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.SerializeToString,
        response_deserializer=RCCommon__pb2.SingleResp.FromString,
        )
    self.createPoint = channel.unary_unary(
        '/resourcecenter.RCPointService/createPoint',
        request_serializer=RCPointService__pb2.Point.SerializeToString,
        response_deserializer=RCCommon__pb2.SingleResp.FromString,
        )
    self.updatePoint = channel.unary_unary(
        '/resourcecenter.RCPointService/updatePoint',
        request_serializer=RCPointService__pb2.Point.SerializeToString,
        response_deserializer=RCCommon__pb2.EmptyResp.FromString,
        )
    self.deletePoint = channel.unary_unary(
        '/resourcecenter.RCPointService/deletePoint',
        request_serializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.SerializeToString,
        response_deserializer=RCCommon__pb2.EmptyResp.FromString,
        )
    self.upGradePoint = channel.unary_unary(
        '/resourcecenter.RCPointService/upGradePoint',
        request_serializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.SerializeToString,
        response_deserializer=RCCommon__pb2.EmptyResp.FromString,
        )
    self.downGradePoint = channel.unary_unary(
        '/resourcecenter.RCPointService/downGradePoint',
        request_serializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.SerializeToString,
        response_deserializer=RCCommon__pb2.EmptyResp.FromString,
        )
    self.upOrderPoint = channel.unary_unary(
        '/resourcecenter.RCPointService/upOrderPoint',
        request_serializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.SerializeToString,
        response_deserializer=RCCommon__pb2.EmptyResp.FromString,
        )
    self.downOrderPoint = channel.unary_unary(
        '/resourcecenter.RCPointService/downOrderPoint',
        request_serializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.SerializeToString,
        response_deserializer=RCCommon__pb2.EmptyResp.FromString,
        )
    self.listPointByChapterIds = channel.unary_unary(
        '/resourcecenter.RCPointService/listPointByChapterIds',
        request_serializer=RCPointService__pb2.ReqPointListByChapterIds.SerializeToString,
        response_deserializer=RCPointService__pb2.RespPointList.FromString,
        )
    self.getPointById = channel.unary_unary(
        '/resourcecenter.RCPointService/getPointById',
        request_serializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.SerializeToString,
        response_deserializer=RCCommon__pb2.SingleResp.FromString,
        )


class RCPointServiceServicer(object):
  """定义服务
  """

  def listPointsBySubjectId(self, request, context):
    """根据科目查知识点(结果message Point)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listPointsJsonBySubjectId(self, request, context):
    """根据科目查知识点(结果message StringValue)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def createPoint(self, request, context):
    """新建知识点(结果message Int32Value)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updatePoint(self, request, context):
    """修改知识点
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deletePoint(self, request, context):
    """删除知识点
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def upGradePoint(self, request, context):
    """升级
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def downGradePoint(self, request, context):
    """降级
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def upOrderPoint(self, request, context):
    """升序
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def downOrderPoint(self, request, context):
    """降序
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listPointByChapterIds(self, request, context):
    """根据多个章节id查询关联的知识点列表
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getPointById(self, request, context):
    """根据知识点id查知识点信息
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RCPointServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'listPointsBySubjectId': grpc.unary_unary_rpc_method_handler(
          servicer.listPointsBySubjectId,
          request_deserializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.FromString,
          response_serializer=RCCommon__pb2.ListResp.SerializeToString,
      ),
      'listPointsJsonBySubjectId': grpc.unary_unary_rpc_method_handler(
          servicer.listPointsJsonBySubjectId,
          request_deserializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.FromString,
          response_serializer=RCCommon__pb2.SingleResp.SerializeToString,
      ),
      'createPoint': grpc.unary_unary_rpc_method_handler(
          servicer.createPoint,
          request_deserializer=RCPointService__pb2.Point.FromString,
          response_serializer=RCCommon__pb2.SingleResp.SerializeToString,
      ),
      'updatePoint': grpc.unary_unary_rpc_method_handler(
          servicer.updatePoint,
          request_deserializer=RCPointService__pb2.Point.FromString,
          response_serializer=RCCommon__pb2.EmptyResp.SerializeToString,
      ),
      'deletePoint': grpc.unary_unary_rpc_method_handler(
          servicer.deletePoint,
          request_deserializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.FromString,
          response_serializer=RCCommon__pb2.EmptyResp.SerializeToString,
      ),
      'upGradePoint': grpc.unary_unary_rpc_method_handler(
          servicer.upGradePoint,
          request_deserializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.FromString,
          response_serializer=RCCommon__pb2.EmptyResp.SerializeToString,
      ),
      'downGradePoint': grpc.unary_unary_rpc_method_handler(
          servicer.downGradePoint,
          request_deserializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.FromString,
          response_serializer=RCCommon__pb2.EmptyResp.SerializeToString,
      ),
      'upOrderPoint': grpc.unary_unary_rpc_method_handler(
          servicer.upOrderPoint,
          request_deserializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.FromString,
          response_serializer=RCCommon__pb2.EmptyResp.SerializeToString,
      ),
      'downOrderPoint': grpc.unary_unary_rpc_method_handler(
          servicer.downOrderPoint,
          request_deserializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.FromString,
          response_serializer=RCCommon__pb2.EmptyResp.SerializeToString,
      ),
      'listPointByChapterIds': grpc.unary_unary_rpc_method_handler(
          servicer.listPointByChapterIds,
          request_deserializer=RCPointService__pb2.ReqPointListByChapterIds.FromString,
          response_serializer=RCPointService__pb2.RespPointList.SerializeToString,
      ),
      'getPointById': grpc.unary_unary_rpc_method_handler(
          servicer.getPointById,
          request_deserializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.FromString,
          response_serializer=RCCommon__pb2.SingleResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'resourcecenter.RCPointService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
