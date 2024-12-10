from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/platform-trident.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_platform = resolve('platform')
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
    if t_2((undefined(name='platform') if l_0_platform is missing else l_0_platform)):
        pass
        for l_1_profile in t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'trident'), 'mmu'), 'queue_profiles'), 'name'):
            _loop_vars = {}
            pass
            yield '!\nplatform trident mmu queue profile '
            yield str(environment.getattr(l_1_profile, 'name'))
            yield '\n'
            for l_2_queue in t_1(environment.getattr(l_1_profile, 'unicast_queues'), 'id'):
                l_2_reserved_cli = resolve('reserved_cli')
                _loop_vars = {}
                pass
                if t_2(environment.getattr(l_2_queue, 'reserved')):
                    pass
                    l_2_reserved_cli = str_join(('egress unicast queue ', environment.getattr(l_2_queue, 'id'), ' reserved', ))
                    _loop_vars['reserved_cli'] = l_2_reserved_cli
                    if t_2(environment.getattr(l_2_queue, 'unit')):
                        pass
                        l_2_reserved_cli = str_join(((undefined(name='reserved_cli') if l_2_reserved_cli is missing else l_2_reserved_cli), ' ', environment.getattr(l_2_queue, 'unit'), ))
                        _loop_vars['reserved_cli'] = l_2_reserved_cli
                    l_2_reserved_cli = str_join(((undefined(name='reserved_cli') if l_2_reserved_cli is missing else l_2_reserved_cli), ' ', environment.getattr(l_2_queue, 'reserved'), ))
                    _loop_vars['reserved_cli'] = l_2_reserved_cli
                    yield '    '
                    yield str((undefined(name='reserved_cli') if l_2_reserved_cli is missing else l_2_reserved_cli))
                    yield '\n'
                if t_2(environment.getattr(l_2_queue, 'threshold')):
                    pass
                    yield '    egress unicast queue '
                    yield str(environment.getattr(l_2_queue, 'id'))
                    yield ' threshold '
                    yield str(environment.getattr(l_2_queue, 'threshold'))
                    yield '\n'
                if t_2(environment.getattr(l_2_queue, 'drop')):
                    pass
                    yield '    egress unicast queue '
                    yield str(environment.getattr(l_2_queue, 'id'))
                    yield ' drop-precedence '
                    yield str(environment.getattr(environment.getattr(l_2_queue, 'drop'), 'precedence'))
                    yield ' drop-threshold '
                    yield str(environment.getattr(environment.getattr(l_2_queue, 'drop'), 'threshold'))
                    yield '\n'
            l_2_queue = l_2_reserved_cli = missing
            for l_2_queue in t_1(environment.getattr(l_1_profile, 'multicast_queues'), 'id'):
                l_2_reserved_cli = resolve('reserved_cli')
                _loop_vars = {}
                pass
                if t_2(environment.getattr(l_2_queue, 'reserved')):
                    pass
                    l_2_reserved_cli = str_join(('egress multicast queue ', environment.getattr(l_2_queue, 'id'), ' reserved', ))
                    _loop_vars['reserved_cli'] = l_2_reserved_cli
                    if t_2(environment.getattr(l_2_queue, 'unit')):
                        pass
                        l_2_reserved_cli = str_join(((undefined(name='reserved_cli') if l_2_reserved_cli is missing else l_2_reserved_cli), ' ', environment.getattr(l_2_queue, 'unit'), ))
                        _loop_vars['reserved_cli'] = l_2_reserved_cli
                    l_2_reserved_cli = str_join(((undefined(name='reserved_cli') if l_2_reserved_cli is missing else l_2_reserved_cli), ' ', environment.getattr(l_2_queue, 'reserved'), ))
                    _loop_vars['reserved_cli'] = l_2_reserved_cli
                    yield '    '
                    yield str((undefined(name='reserved_cli') if l_2_reserved_cli is missing else l_2_reserved_cli))
                    yield '\n'
                if t_2(environment.getattr(l_2_queue, 'threshold')):
                    pass
                    yield '    egress multicast queue '
                    yield str(environment.getattr(l_2_queue, 'id'))
                    yield ' threshold '
                    yield str(environment.getattr(l_2_queue, 'threshold'))
                    yield '\n'
                if t_2(environment.getattr(l_2_queue, 'drop')):
                    pass
                    yield '    egress multicast queue '
                    yield str(environment.getattr(l_2_queue, 'id'))
                    yield ' drop-precedence '
                    yield str(environment.getattr(environment.getattr(l_2_queue, 'drop'), 'precedence'))
                    yield ' drop-threshold '
                    yield str(environment.getattr(environment.getattr(l_2_queue, 'drop'), 'threshold'))
                    yield '\n'
            l_2_queue = l_2_reserved_cli = missing
        l_1_profile = missing

blocks = {}
debug_info = '7=24&8=26&10=30&11=32&12=36&13=38&14=40&15=42&17=44&18=47&20=49&21=52&23=56&24=59&27=66&28=70&29=72&30=74&31=76&33=78&34=81&36=83&37=86&39=90&40=93'