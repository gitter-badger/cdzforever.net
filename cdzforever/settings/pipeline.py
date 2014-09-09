# -*- coding: utf-8 -*-

PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': {
            'css/bootstrap.css',
            'css/bootstrap-theme.css',
        },
        'output_filename': 'css/bootstrap.min.css',
    }
}

PIPELINE_JS = {
    'jquery': {
        'source_filenames': {
            'js/jquery-2.1.1.js',
        },
        'output_filename': 'css/jquery.min.css',
    },

    'bootstrap': {
        'source_filenames': {
            'js/bootstrap.js',
        },
        'output_filename': 'js/bootstrap.min.js',
    }
}
