from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/trackers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_trackers = resolve('trackers')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='trackers') if l_0_trackers is missing else l_0_trackers)):
        pass
        yield '!\n'
        for l_1_tracked_obj in t_2((undefined(name='trackers') if l_0_trackers is missing else l_0_trackers), 'name'):
            l_1_tracked_obj_cli = resolve('tracked_obj_cli')
            _loop_vars = {}
            pass
            if (t_3(environment.getattr(l_1_tracked_obj, 'name')) and t_3(environment.getattr(l_1_tracked_obj, 'interface'))):
                pass
                l_1_tracked_obj_cli = str_join(('track ', environment.getattr(l_1_tracked_obj, 'name'), ' interface ', environment.getattr(l_1_tracked_obj, 'interface'), ' ', t_1(environment.getattr(l_1_tracked_obj, 'tracked_property'), 'line-protocol'), ))
                _loop_vars['tracked_obj_cli'] = l_1_tracked_obj_cli
                yield str((undefined(name='tracked_obj_cli') if l_1_tracked_obj_cli is missing else l_1_tracked_obj_cli))
                yield '\n'
        l_1_tracked_obj = l_1_tracked_obj_cli = missing

blocks = {}
debug_info = '7=30&9=33&10=37&11=39&12=41'