from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/management-api-models.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_api_models = resolve('management_api_models')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['lower']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'lower' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='management_api_models') if l_0_management_api_models is missing else l_0_management_api_models)):
        pass
        yield '!\nmanagement api models\n'
        for l_1_provider in t_1(environment.getattr((undefined(name='management_api_models') if l_0_management_api_models is missing else l_0_management_api_models), 'providers'), 'name'):
            _loop_vars = {}
            pass
            if (t_3(environment.getattr(l_1_provider, 'name')) and (t_2(environment.getattr(l_1_provider, 'name')) in ['smash', 'sysdb'])):
                pass
                yield '   !\n   provider '
                yield str(environment.getattr(l_1_provider, 'name'))
                yield '\n'
                for l_2_path in t_1(environment.getattr(l_1_provider, 'paths'), 'path'):
                    l_2_provider_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_provider_cli = str_join(('path ', environment.getattr(l_2_path, 'path'), ))
                    _loop_vars['provider_cli'] = l_2_provider_cli
                    if t_3(environment.getattr(l_2_path, 'disabled'), True):
                        pass
                        l_2_provider_cli = str_join(((undefined(name='provider_cli') if l_2_provider_cli is missing else l_2_provider_cli), ' disabled', ))
                        _loop_vars['provider_cli'] = l_2_provider_cli
                    yield '      '
                    yield str((undefined(name='provider_cli') if l_2_provider_cli is missing else l_2_provider_cli))
                    yield '\n'
                l_2_path = l_2_provider_cli = missing
        l_1_provider = missing

blocks = {}
debug_info = '7=30&10=33&11=36&13=39&14=41&15=45&16=47&17=49&19=52'