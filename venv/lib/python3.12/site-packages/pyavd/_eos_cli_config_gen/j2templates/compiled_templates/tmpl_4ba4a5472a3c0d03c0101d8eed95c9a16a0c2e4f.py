from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/link-tracking-groups.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_link_tracking_groups = resolve('link_tracking_groups')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='link_tracking_groups') if l_0_link_tracking_groups is missing else l_0_link_tracking_groups)):
        pass
        yield '!\n'
        for l_1_link_tracking_group in t_1((undefined(name='link_tracking_groups') if l_0_link_tracking_groups is missing else l_0_link_tracking_groups), 'name'):
            _loop_vars = {}
            pass
            if t_2(environment.getattr(l_1_link_tracking_group, 'name')):
                pass
                yield 'link tracking group '
                yield str(environment.getattr(l_1_link_tracking_group, 'name'))
                yield '\n'
                if t_2(environment.getattr(l_1_link_tracking_group, 'links_minimum')):
                    pass
                    yield '   links minimum '
                    yield str(environment.getattr(l_1_link_tracking_group, 'links_minimum'))
                    yield '\n'
                if t_2(environment.getattr(l_1_link_tracking_group, 'recovery_delay')):
                    pass
                    yield '   recovery delay '
                    yield str(environment.getattr(l_1_link_tracking_group, 'recovery_delay'))
                    yield '\n'
        l_1_link_tracking_group = missing

blocks = {}
debug_info = '7=24&9=27&10=30&11=33&12=35&13=38&15=40&16=43'