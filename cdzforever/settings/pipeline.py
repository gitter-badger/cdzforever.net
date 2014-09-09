# -*- coding: utf-8 -*-

PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': {
            'bower_components/bootstrap/dist/css/bootstrap.css',
            'bower_components/bootstrap/dist/css/bootstrap-theme.css',
        },
        'output_filename': 'css/bootstrap.min.css',
    }
}

PIPELINE_JS = {
    'jquery': {
        'source_filenames': {
            'bower_components/jquery/dist/jquery.js',
        },
        'output_filename': 'js/jquery.min.css',
    },

    'bootstrap': {
        'source_filenames': {
            'bower_components/bootstrap/dist/js/bootstrap.js',
        },
        'output_filename': 'js/bootstrap.min.js',
    }
}
