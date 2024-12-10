from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/errdisable.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_errdisable = resolve('errdisable')
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
    try:
        t_3 = environment.tests['defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'defined' found.")
    pass
    if t_2((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable)):
        pass
        yield '\n## Errdisable\n\n### Errdisable Summary\n\n'
        if t_3(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery')):
            pass
            if t_3(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'detect'), 'causes')):
                pass
                yield '|  Detect Cause | Enabled |\n| ------------- | ------- |\n'
                for l_1_cause in t_1(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'detect'), 'causes')):
                    _loop_vars = {}
                    pass
                    if (l_1_cause == 'acl'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True |\n'
                    elif (l_1_cause == 'arp-inspection'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True |\n'
                    elif (l_1_cause == 'dot1x'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True |\n'
                    elif (l_1_cause == 'link-change'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True |\n'
                    elif (l_1_cause == 'tapagg'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True |\n'
                    elif (l_1_cause == 'xcvr-misconfigured'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True |\n'
                    elif (l_1_cause == 'xcvr-overheat'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True |\n'
                    elif (l_1_cause == 'xcvr-power-unsupported'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True |\n'
                l_1_cause = missing
            yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval')):
                pass
            if t_3(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'causes')):
                pass
                yield '|  Detect Cause | Enabled | Interval |\n| ------------- | ------- | -------- |\n'
                for l_1_cause in t_1(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'causes')):
                    _loop_vars = {}
                    pass
                    if (l_1_cause == 'arp-inspection'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'bpduguard'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'dot1x'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'hitless-reload-down'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'lacp-rate-limit'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'link-flap'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'no-internal-vlan'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'portchannelguard'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'portsec'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'speed-misconfigured'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'tapagg'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'uplink-failure-detection'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'xcvr-misconfigured'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'xcvr-overheat'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'xcvr-power-unsupported'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                    elif (l_1_cause == 'xcvr-unsupported'):
                        pass
                        yield '| '
                        yield str(l_1_cause)
                        yield ' | True | '
                        yield str(environment.getattr(environment.getattr((undefined(name='errdisable') if l_0_errdisable is missing else l_0_errdisable), 'recovery'), 'interval'))
                        yield ' |\n'
                l_1_cause = missing
        yield '\n```eos\n'
        template = environment.get_template('eos/errdisable.j2', 'documentation/errdisable.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&13=33&14=35&17=38&18=41&19=44&20=46&21=49&22=51&23=54&24=56&25=59&26=61&27=64&28=66&29=69&30=71&31=74&32=76&33=79&38=83&40=85&43=88&44=91&45=94&46=98&47=101&48=105&49=108&50=112&51=115&52=119&53=122&54=126&55=129&56=133&57=136&58=140&59=143&60=147&61=150&62=154&63=157&64=161&65=164&66=168&67=171&68=175&69=178&70=182&71=185&72=189&73=192&74=196&75=199&82=205'