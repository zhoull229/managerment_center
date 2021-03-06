# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import RCGradeService_pb2 as RCGradeService__pb2


class RCGradeServiceStub(object):
  """年级相关的
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.listGrade = channel.unary_unary(
        '/resourcecenter.RCGradeService/listGrade',
        request_serializer=RCGradeService__pb2.RequestGradeList.SerializeToString,
        response_deserializer=RCGradeService__pb2.ResponseGradeList.FromString,
        )


class RCGradeServiceServicer(object):
  """年级相关的
  """

  def listGrade(self, request, context):
    """查询年级列表
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RCGradeServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'listGrade': grpc.unary_unary_rpc_method_handler(
          servicer.listGrade,
          request_deserializer=RCGradeService__pb2.RequestGradeList.FromString,
          response_serializer=RCGradeService__pb2.ResponseGradeList.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'resourcecenter.RCGradeService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
