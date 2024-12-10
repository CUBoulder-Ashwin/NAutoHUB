from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/config-comment.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_config_comment = resolve('config_comment')
    l_0_multiline_comment = resolve('multiline_comment')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='config_comment') if l_0_config_comment is missing else l_0_config_comment)):
        pass
        yield '!\n'
        l_0_multiline_comment = context.call(environment.getattr((undefined(name='config_comment') if l_0_config_comment is missing else l_0_config_comment), 'split'), '\n')
        context.vars['multiline_comment'] = l_0_multiline_comment
        context.exported_vars.add('multiline_comment')
        for l_1_comment in (undefined(name='multiline_comment') if l_0_multiline_comment is missing else l_0_multiline_comment):
            _loop_vars = {}
            pass
            yield '!'
            yield str(l_1_comment)
            yield '\n'
        l_1_comment = missing

blocks = {}
debug_info = '7=19&9=22&10=25&11=29'