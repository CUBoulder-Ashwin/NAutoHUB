from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos-device-documentation.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_eos_cli_config_gen_documentation = resolve('eos_cli_config_gen_documentation')
    l_0_hostname = resolve('hostname')
    l_0_inventory_hostname = resolve('inventory_hostname')
    l_0_hide_passwords = missing
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    pass
    l_0_hide_passwords = t_1(environment.getattr((undefined(name='eos_cli_config_gen_documentation') if l_0_eos_cli_config_gen_documentation is missing else l_0_eos_cli_config_gen_documentation), 'hide_passwords'), True)
    context.vars['hide_passwords'] = l_0_hide_passwords
    context.exported_vars.add('hide_passwords')
    yield '# '
    yield str(t_1((undefined(name='hostname') if l_0_hostname is missing else l_0_hostname), (undefined(name='inventory_hostname') if l_0_inventory_hostname is missing else l_0_inventory_hostname)))
    yield '\n\n## Table of Contents\n\n<!-- toc -->\n<!-- toc -->\n'
    template = environment.get_template('documentation/management.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/cvx.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/authentication.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/address-locking.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/management-security.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/prompt.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/aliases.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/dhcp-relay.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/dhcp-servers.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/boot.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/monitoring.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/monitor-connectivity.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/monitor-layer1.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/tcam-profile.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/link-tracking-groups.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/mlag-configuration.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/lldp.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/l2-protocol-forwarding.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/lacp.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/spanning-tree.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/sync-e.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/vlan-internal-order.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/vlans.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/mac-address-table.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/ip-security.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/interfaces.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/switchport-port-security.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/routing.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/bfd.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/mpls.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/patch-panel.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/queue-monitor.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/multicast.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/filters.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/dot1x.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/poe.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/acl.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/vrfs.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/virtual-source-nat-vrfs.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/platform.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/system-l1.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/application-traffic-recognition.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/router-segment-security.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/router-path-selection.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/router-internet-exit.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/router-l2-vpn.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/ip-dhcp-relay.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/ipv6-dhcp-relay.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/ip-dhcp-snooping.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/ip-nat.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/errdisable.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/mac-security.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/traffic-policies.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/quality-of-service.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/monitor-telemetry-influx.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/priority-flow-control.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/stun.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/maintenance-mode.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/eos-cli.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event

blocks = {}
debug_info = '7=21&8=25&15=27&17=30&19=33&21=36&23=39&25=42&27=45&29=48&31=51&33=54&35=57&37=60&39=63&41=66&43=69&45=72&47=75&49=78&51=81&53=84&55=87&57=90&59=93&61=96&63=99&65=102&67=105&69=108&71=111&73=114&75=117&77=120&79=123&81=126&83=129&85=132&87=135&89=138&91=141&93=144&95=147&97=150&99=153&101=156&103=159&105=162&107=165&109=168&111=171&113=174&115=177&117=180&119=183&121=186&123=189&125=192&127=195&129=198&131=201'