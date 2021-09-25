from conduit.apps.core.renderers import ConduitJSONRenderer


class HistoryJSONRenderer(ConduitJSONRenderer):
    object_label = 'history'
    pagination_object_label = 'historys'
    pagination_count_label = 'historysCount'