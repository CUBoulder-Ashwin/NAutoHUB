from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos-intended-config.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_eos_cli_config_gen_configuration = resolve('eos_cli_config_gen_configuration')
    l_0_hide_passwords = missing
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    pass
    l_0_hide_passwords = t_1(environment.getattr((undefined(name='eos_cli_config_gen_configuration') if l_0_eos_cli_config_gen_configuration is missing else l_0_eos_cli_config_gen_configuration), 'hide_passwords'), False)
    context.vars['hide_passwords'] = l_0_hide_passwords
    context.exported_vars.add('hide_passwords')
    template = environment.get_template('eos/rancid-content-type.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/config-comment.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/boot.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/enable-password.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/aaa-root.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/local-users.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/address-locking.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/agents.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/hardware.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/service-routing-configuration-bgp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/prompt.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/terminal.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/aliases.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/logging-event-storm-control.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/daemon-terminattr.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/daemons.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/dhcp-relay.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-dhcp-relay.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ipv6-dhcp-relay.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/dhcp-servers.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-dhcp-snooping.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/switchport-default.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/vlan-internal-order.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/errdisable.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/event-monitor.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/flow-tracking.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-igmp-snooping.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/logging-event-congestion-drops.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/load-interval.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/transceiver-qsfp-default-mode.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/interface-defaults.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/service-routing-protocols-model.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/l2-protocol-forwarding.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/lacp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/queue-monitor-length.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/monitor-layer1.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/link-tracking-groups.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/lldp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/logging.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/match-list-input.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/mcs-client.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/monitor-server-radius.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/platform-trident.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-nat-part1.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/hostname.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-domain-lookup.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-name-servers.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/dns-domain.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/domain-list.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/aaa-server-groups-ldap.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/trackers.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/poe.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/switchport-port-security.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ptp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/qos-profiles.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/redundancy.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-adaptive-virtual-topology.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-internet-exit.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-l2-vpn.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-path-selection.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-service-insertion.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/platform.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/sflow.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/snmp-server.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/hardware-speed-groups.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/spanning-tree.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/sync-e.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/service-unsupported-transceiver.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/system-l1.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/tap-aggregation.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/clock.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/vlans.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/vrfs.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/bgp-groups.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/queue-monitor-streaming.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/banners.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/management-accounts.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/management-api-http.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/management-console.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/management-cvx.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/management-defaults.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/management-api-gnmi.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/management-api-models.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/management-security.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/radius-server.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/aaa-server-groups-radius.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/tacacs-servers.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/aaa-server-groups-tacacs-plus.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/aaa.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/cvx.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/dot1x.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/monitor-telemetry-influx.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-security.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/mac-security.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/port-channel-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/dps-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ethernet-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/loopback-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/management-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/tunnel-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/vlan-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/vxlan-interface.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/tcam-profile.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/application-traffic-recognition.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/monitor-connectivity.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/mac-address-table-aging-time.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/event-handlers.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-segment-security.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/interface-groups.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/interface-profiles.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-virtual-router-mac-address.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/virtual-source-nat-vrfs.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ipv6-access-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ipv6-standard-access-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/access-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-access-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/class-maps-pbr.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/standard-access-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-routing.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-icmp-redirect.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-hardware.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-routing-vrfs.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ipv6-icmp-redirect.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/as-path.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-community-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/community-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-extcommunity-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-extcommunity-lists-regexp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/dynamic-prefix-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/prefix-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ipv6-prefix-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ipv6-unicast-routing.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ipv6-hardware.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ipv6-unicast-routing-vrfs.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ipv6-neighbors.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/mac-access-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/system.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/mac-address-table-notification.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/maintenance.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/monitor-sessions.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/monitor-session-default-encapsulation-gre.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/mlag-configuration.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/static-routes.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/arp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ipv6-static-routes.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/mpls.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-nat-part2.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-client-source-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ntp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/patch-panel.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/policy-maps-pbr.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/monitor-telemetry-postcard-policy.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/qos.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/class-maps.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/policy-maps-copp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/policy-maps-qos.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/priority-flow-control.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-radius-source-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/roles.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/route-maps.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/peer-filters.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-bfd.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-bgp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-general.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-traffic-engineering.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-igmp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-isis.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-multicast.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-ospf.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-pim-sparse-mode.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/router-msdp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/stun.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/ip-tacacs-source-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/traffic-policies.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/platform-apply.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/vmtracer-sessions.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/dot1x_part2.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/management-ssh.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/management-tech-support.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/eos-cli.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('eos/end.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event

blocks = {}
debug_info = '8=19&9=22&10=25&12=28&14=31&16=34&18=37&20=40&22=43&24=46&26=49&28=52&30=55&32=58&34=61&36=64&38=67&40=70&42=73&44=76&46=79&48=82&50=85&52=88&54=91&56=94&58=97&60=100&62=103&64=106&66=109&68=112&70=115&72=118&74=121&76=124&78=127&80=130&82=133&84=136&86=139&88=142&90=145&92=148&94=151&96=154&98=157&100=160&102=163&104=166&106=169&108=172&110=175&112=178&114=181&116=184&118=187&120=190&122=193&124=196&126=199&128=202&130=205&132=208&134=211&136=214&138=217&140=220&142=223&144=226&146=229&148=232&150=235&152=238&154=241&156=244&158=247&160=250&162=253&164=256&166=259&168=262&170=265&172=268&174=271&176=274&178=277&180=280&182=283&184=286&186=289&188=292&190=295&192=298&194=301&196=304&198=307&200=310&202=313&204=316&206=319&208=322&210=325&212=328&214=331&216=334&218=337&220=340&222=343&224=346&226=349&228=352&230=355&232=358&234=361&236=364&238=367&240=370&242=373&244=376&246=379&248=382&250=385&252=388&254=391&256=394&258=397&260=400&262=403&264=406&266=409&268=412&270=415&272=418&274=421&276=424&278=427&280=430&282=433&284=436&286=439&287=442&289=445&291=448&293=451&295=454&297=457&299=460&301=463&303=466&305=469&307=472&309=475&311=478&313=481&315=484&317=487&319=490&321=493&323=496&325=499&327=502&329=505&331=508&333=511&335=514&337=517&339=520&341=523&343=526&345=529&347=532&349=535&351=538&353=541&355=544&357=547&359=550&361=553&363=556&365=559&367=562'