# -*- coding: utf-8 -*-

#   Copyright 2015-2017 Lionheart Software LLC
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from .metadata import (
    __author__,
    __copyright__,
    __email__,
    __license__,
    __maintainer__,
    __version__,
)

from .bigstore import (
    filter_smudge,
    filter_clean,
    init,
    push,
    pull,
    log,
    fetch
)

import backends

__all__ = [
    '__author__', '__copyright__', '__email__', '__license__',
    '__maintainer__', '__version__', 'filter_smudge', 'filter_clean',
    'init', 'push', 'pull', 'backends', 'log', 'fetch'
]

