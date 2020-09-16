# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

c.auto_save.session = True


# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
c.content.notifications = False

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
# Directory to save downloads to. If unset, a sensible OS-specific
# default is used.
# Type: Directory
c.downloads.location.directory = '~/downloads'

# Duration (in milliseconds) to wait before removing finished downloads.
# If set to -1, downloads are never removed.
# Type: Int
c.downloads.remove_finished = 0

# open tabs in background
c.tabs.background = True
c.input.partial_timeout = 20000
c.tabs.show = 'multiple'
c.hints.auto_follow='always'

# Bindings
config.unbind('d')
config.unbind('u')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('x','tab-close')
config.bind('X','undo')
config.bind('d','scroll-px 0 350')
config.bind('u','scroll-px 0 -350')
config.bind('gi','hint inputs')
config.bind('yf','hint links yank')
config.bind('ge','set-cmd-text :open {url:pretty}')
config.bind('W','tab-give')
config.bind(';v','hint links spawn vlc {hint-url}')
config.bind(';V','hint links spawn vlc {hint-url} --no-video')
config.bind('yv','spawn vlc {url:pretty}')
config.bind('yV','spawn vlc {url:pretty} --no-video')


# vim
c.editor.command =['st','-e','vim','-f','{file}','-c','normal {line}G{column0}l']

#theme
config.source('qutewal.py')
import glob

c.content.user_stylesheets = glob.glob('/home/meta/.config/qutebrowser/user-styles/*')
# force dark theme
# c.qt.args=["blink-settings=darkMode=4"]
c.content.ssl_strict=True
# c.colors.webpage.darkmode.enabled=True
# FONT
c.fonts.default_family="FiraCode Nerd Font"
