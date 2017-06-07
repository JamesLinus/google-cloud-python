# Copyright 2017, Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

from google.cloud.gapic.vision.v1 import image_annotator_client as iac
from google.cloud.gapic.vision.v1 import enums

from google.cloud.vision.helpers import VisionHelpers
from google.cloud.vision_v1 import types


@add_single_feature_methods
class ImageAnnotatorClient(VisionHelpers, iac.ImageAnnotatorClient):
    __doc__ = iac.ImageAnnotatorClient.__doc__
    enums = enums


__all__ = (
    'enums',
    'ImageAnnotatorClient',
    'types',
)
