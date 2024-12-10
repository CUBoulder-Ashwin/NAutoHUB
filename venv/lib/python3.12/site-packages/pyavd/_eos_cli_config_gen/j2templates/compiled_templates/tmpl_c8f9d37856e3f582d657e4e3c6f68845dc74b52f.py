from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/maintenance.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_maintenance = resolve('maintenance')
    l_0_first_line = missing
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
    l_0_first_line = {'flag': True}
    context.vars['first_line'] = l_0_first_line
    context.exported_vars.add('first_line')
    if t_2((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance)):
        pass
        yield '!\nmaintenance\n'
        l_1_loop = missing
        for l_1_bgp_profile, l_1_loop in LoopContext(t_1(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'bgp_profiles'), 'name'), undefined):
            l_1_first_line = l_0_first_line
            _loop_vars = {}
            pass
            if (environment.getattr(l_1_loop, 'index0') > 0):
                pass
                yield '   !\n'
            l_1_first_line = {'flag': False}
            _loop_vars['first_line'] = l_1_first_line
            yield '   profile bgp '
            yield str(environment.getattr(l_1_bgp_profile, 'name'))
            yield '\n'
            if t_2(environment.getattr(environment.getattr(l_1_bgp_profile, 'initiator'), 'route_map_inout')):
                pass
                yield '      initiator route-map '
                yield str(environment.getattr(environment.getattr(l_1_bgp_profile, 'initiator'), 'route_map_inout'))
                yield ' inout\n'
        l_1_loop = l_1_bgp_profile = l_1_first_line = missing
        if t_2(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'default_bgp_profile')):
            pass
            l_0_first_line = {'flag': False}
            context.vars['first_line'] = l_0_first_line
            context.exported_vars.add('first_line')
            yield '   profile bgp '
            yield str(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'default_bgp_profile'))
            yield ' default\n'
        if t_2(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'default_interface_profile')):
            pass
            l_0_first_line = {'flag': False}
            context.vars['first_line'] = l_0_first_line
            context.exported_vars.add('first_line')
            yield '   profile interface '
            yield str(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'default_interface_profile'))
            yield ' default\n'
        if t_2(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'default_unit_profile')):
            pass
            l_0_first_line = {'flag': False}
            context.vars['first_line'] = l_0_first_line
            context.exported_vars.add('first_line')
            yield '   profile unit '
            yield str(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'default_unit_profile'))
            yield ' default\n'
        for l_1_interface_profile in t_1(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'interface_profiles'), 'name'):
            l_1_first_line = l_0_first_line
            _loop_vars = {}
            pass
            if (not environment.getattr((undefined(name='first_line') if l_1_first_line is missing else l_1_first_line), 'flag')):
                pass
                yield '   !\n'
            l_1_first_line = {'flag': False}
            _loop_vars['first_line'] = l_1_first_line
            yield '   profile interface '
            yield str(environment.getattr(l_1_interface_profile, 'name'))
            yield '\n'
            if t_2(environment.getattr(environment.getattr(l_1_interface_profile, 'rate_monitoring'), 'load_interval')):
                pass
                yield '      rate-monitoring load-interval '
                yield str(environment.getattr(environment.getattr(l_1_interface_profile, 'rate_monitoring'), 'load_interval'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr(l_1_interface_profile, 'rate_monitoring'), 'threshold')):
                pass
                yield '      rate-monitoring threshold '
                yield str(environment.getattr(environment.getattr(l_1_interface_profile, 'rate_monitoring'), 'threshold'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr(l_1_interface_profile, 'shutdown'), 'max_delay')):
                pass
                yield '      shutdown max-delay '
                yield str(environment.getattr(environment.getattr(l_1_interface_profile, 'shutdown'), 'max_delay'))
                yield '\n'
        l_1_interface_profile = l_1_first_line = missing
        for l_1_unit_profile in t_1(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'unit_profiles'), 'name'):
            l_1_first_line = l_0_first_line
            _loop_vars = {}
            pass
            if (not environment.getattr((undefined(name='first_line') if l_1_first_line is missing else l_1_first_line), 'flag')):
                pass
                yield '   !\n'
            l_1_first_line = {'flag': False}
            _loop_vars['first_line'] = l_1_first_line
            yield '   profile unit '
            yield str(environment.getattr(l_1_unit_profile, 'name'))
            yield '\n'
            if t_2(environment.getattr(environment.getattr(l_1_unit_profile, 'on_boot'), 'duration')):
                pass
                yield '      on-boot duration '
                yield str(environment.getattr(environment.getattr(l_1_unit_profile, 'on_boot'), 'duration'))
                yield '\n'
        l_1_unit_profile = l_1_first_line = missing
        for l_1_unit in t_1(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'units'), 'name'):
            l_1_first_line = l_0_first_line
            _loop_vars = {}
            pass
            if (not environment.getattr((undefined(name='first_line') if l_1_first_line is missing else l_1_first_line), 'flag')):
                pass
                yield '   !\n'
            l_1_first_line = {'flag': False}
            _loop_vars['first_line'] = l_1_first_line
            yield '   unit '
            yield str(environment.getattr(l_1_unit, 'name'))
            yield '\n'
            for l_2_bgp_group in t_1(environment.getattr(environment.getattr(l_1_unit, 'groups'), 'bgp_groups')):
                _loop_vars = {}
                pass
                yield '      group bgp '
                yield str(l_2_bgp_group)
                yield '\n'
            l_2_bgp_group = missing
            for l_2_interface_group in t_1(environment.getattr(environment.getattr(l_1_unit, 'groups'), 'interface_groups')):
                _loop_vars = {}
                pass
                yield '      group interface '
                yield str(l_2_interface_group)
                yield '\n'
            l_2_interface_group = missing
            if t_2(environment.getattr(l_1_unit, 'profile')):
                pass
                yield '      profile unit '
                yield str(environment.getattr(l_1_unit, 'profile'))
                yield '\n'
            if t_2(environment.getattr(l_1_unit, 'quiesce'), True):
                pass
                yield '      quiesce\n'
            elif t_2(environment.getattr(l_1_unit, 'quiesce'), False):
                pass
                yield '      no quiesce\n'
        l_1_unit = l_1_first_line = missing

blocks = {}
debug_info = '7=25&8=28&11=32&12=36&15=39&16=42&17=44&18=47&21=50&22=52&23=56&25=58&26=60&27=64&29=66&30=68&31=72&33=74&34=78&37=81&38=84&39=86&40=89&42=91&43=94&45=96&46=99&49=102&50=106&53=109&54=112&55=114&56=117&59=120&60=124&63=127&64=130&65=132&66=136&68=139&69=143&71=146&72=149&74=151&76=154'