# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'JSON-to-Excel Documentation'
copyright = '2026, WTSolutions'
author = 'WTSolutions'
release = '6.1.0.0'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser','sphinx_sitemap']
html_baseurl = 'https://json-to-excel.wtsolutions.cn/'
sitemap_url_scheme = "{link}"
html_extra_path = ['robots.txt','ads.txt','baidu_verify_codeva-NQXz6GN9nc.html','ByteDanceVerify.html','llms.txt']

templates_path = ['_templates']
exclude_patterns = []

myst_enable_extensions = ["colon_fence"]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "shibuya"
html_static_path = ['_static']

# 自定义导航链接
# shibuya 主题的导航链接配置项
html_theme_options = {
    "nav_links": [
        {
            "title": "Product File",
            "url": "https://s.wtsolutions.cn/excel-json-product.html",
            "external": True
        },
        {
            "title": "JSON-to-Excel Web App",
            "url": "https://s.wtsolutions.cn/json-to-excel.html",
            "external": True
        },
        {
            "title": "Relates Products",
            "url": "products",
            "children": [
                {
                    "title": "Excel-to-JSON",
                    "url": "https://s.wtsolutions.cn/excel-json-product.html",
                    "external": True
                },
                {
                    "title": "Sheet-to-Doc",
                    "url": "https://s.wtsolutions.cn/sheet-to-doc-product.html",
                    "external": True
                }
            ]
        }
    ]
}

html_context = {
    "languages": [
        ("English", "/en/latest/%s.html", "en"),
        ("中文", "/zh-cn/latest/%s.html", "zh-cn"),
    ]
}
