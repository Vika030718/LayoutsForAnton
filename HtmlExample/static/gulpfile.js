'use strict';

var gulp         = require('gulp'),
    stylus       = require('gulp-stylus'),
    csscomb      = require('gulp-csscomb'),
    autoprefixer = require('gulp-autoprefixer');

gulp.task('transform-stylus', function () {
  return gulp.src('./stylus/[^_]*.styl')
    .pipe(stylus())
    .on('error', function (err) {
      this.emit('end');
    })
    .pipe(autoprefixer({
      browsers: ['> 3%']
    }))
    .pipe(csscomb())
    .pipe(gulp.dest('css'));
});

gulp.task('default', ['transform-stylus'], function () {
  gulp.watch('./stylus/[^_]*.styl', ['transform-stylus']);
});

