# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1405772086.42606
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/bootstrap3/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'sourcelink', u'extra_js', u'belowtitle']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'notes', context._clean_inheritance_tokens(), templateuri=u'annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'notes')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        show_sourcelink = _import_ns.get('show_sourcelink', context.get('show_sourcelink', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        notes = _mako_get_namespace(context, 'notes')
        __M_writer = context.writer()
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(unicode(base.html_headstart()))
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 8
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(unicode(template_hooks['extra_head']()))
        __M_writer(u'\n</head>\n<body>\n\n<!-- Menubar -->\n\n<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n    <div class="container"><!-- This keeps the margins nice -->\n        <div class="navbar-header">\n            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">\n            <span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="')
        # SOURCE LINE 24
        __M_writer(unicode(abs_link('/')))
        __M_writer(u'">\n')
        # SOURCE LINE 25
        if logo_url:
            # SOURCE LINE 26
            __M_writer(u'                <img src="')
            __M_writer(unicode(logo_url))
            __M_writer(u'" alt="')
            __M_writer(unicode(blog_title))
            __M_writer(u'" id="logo">\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        if show_blog_title:
            # SOURCE LINE 30
            __M_writer(u'                <span id="blog-title">')
            __M_writer(unicode(blog_title))
            __M_writer(u'</span>\n')
        # SOURCE LINE 32
        __M_writer(u'            </a>\n        </div><!-- /.navbar-header -->\n        <div class="collapse navbar-collapse navbar-ex1-collapse">\n            <ul class="nav navbar-nav">\n                ')
        # SOURCE LINE 36
        __M_writer(unicode(base.html_navigation_links()))
        __M_writer(u'\n                ')
        # SOURCE LINE 37
        __M_writer(unicode(template_hooks['menu']()))
        __M_writer(u'\n            </ul>\n')
        # SOURCE LINE 39
        if search_form:
            # SOURCE LINE 40
            __M_writer(u'                ')
            __M_writer(unicode(search_form))
            __M_writer(u'\n')
        # SOURCE LINE 42
        __M_writer(u'\n            <ul class="nav navbar-nav navbar-right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        # SOURCE LINE 48
        __M_writer(u'\n')
        # SOURCE LINE 49
        if show_sourcelink:
            # SOURCE LINE 50
            __M_writer(u'                    ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
                context['self'].sourcelink(**pageargs)
            

            __M_writer(u'\n')
        # SOURCE LINE 52
        __M_writer(u'                ')
        __M_writer(unicode(template_hooks['menu_alt']()))
        __M_writer(u'\n            </ul>\n        </div><!-- /.navbar-collapse -->\n    </div><!-- /.container -->\n</nav>\n\n<!-- End of Menubar -->\n\n<div class="container">\n    <div class="body-content">\n        <!--Body content-->\n        <div class="row">\n            ')
        # SOURCE LINE 64
        __M_writer(unicode(template_hooks['page_header']()))
        __M_writer(u'\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 65
        __M_writer(u'\n        </div>\n        <!--End of body content-->\n\n        <footer>\n            ')
        # SOURCE LINE 70
        __M_writer(unicode(content_footer))
        __M_writer(u'\n            ')
        # SOURCE LINE 71
        __M_writer(unicode(template_hooks['page_footer']()))
        __M_writer(u'\n        </footer>\n    </div>\n</div>\n\n')
        # SOURCE LINE 76
        __M_writer(unicode(base.late_load_js()))
        __M_writer(u'\n    <script>jQuery("a.image-reference").colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        # SOURCE LINE 78
        __M_writer(u'\n')
        # SOURCE LINE 79
        if annotations and post and not post.meta('noannotations'):
            # SOURCE LINE 80
            __M_writer(u'        ')
            __M_writer(unicode(notes.code()))
            __M_writer(u'\n')
            # SOURCE LINE 81
        elif not annotations and post and post.meta('annotations'):
            # SOURCE LINE 82
            __M_writer(u'        ')
            __M_writer(unicode(notes.code()))
            __M_writer(u'\n')
        # SOURCE LINE 84
        __M_writer(unicode(body_end))
        __M_writer(u'\n')
        # SOURCE LINE 85
        __M_writer(unicode(template_hooks['body_end']()))
        __M_writer(u'\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def belowtitle():
            return render_belowtitle(context)
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n')
        # SOURCE LINE 45
        if len(translations) > 1:
            # SOURCE LINE 46
            __M_writer(u'                    <li>')
            __M_writer(unicode(base.html_translations()))
            __M_writer(u'</li>\n')
        # SOURCE LINE 48
        __M_writer(u'                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


