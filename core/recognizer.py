# -*- coding: utf-8 -*-
# @Time    : 2017/9/2 13:40
# @Author  : 郑梓斌

import numpy as np

from . import face_alignment


FACE_POINTS = list(range(0, 68))
JAW_POINTS = list(range(0, 17))
LEFT_EYE_POINTS = list(range(36, 42))
LEFT_BROW_POINTS = list(range(17, 22))
RIGHT_EYE_POINTS = list(range(42, 48))
RIGHT_BROW_POINTS = list(range(22, 27))

LEFT_FACE = list(range(0, 9)) + list(range(17, 22))
RIGHT_FACE = list(range(8, 17)) + list(range(22, 27))

JAW_END = 17
FACE_END = 68

OVERLAY_POINTS = [
    LEFT_FACE,
    RIGHT_FACE,
    JAW_POINTS,
]


def face_points(image):
    face_landmarks = face_alignment.landmarks_detector.get_landmarks(image)
    face_landmarks = next(face_landmarks)
    matrix_list = np.matrix(face_landmarks)

    point_list = []
    for p in matrix_list.tolist():
        point_list.append((int(p[0]), int(p[1])))
    return matrix_list, point_list


def matrix_rectangle(left, top, width, height):
    pointer = [
        (left, top),
        (left + width / 2, top),
        (left + width - 1, top),
        (left + width - 1, top + height / 2),
        (left, top + height / 2),
        (left, top + height - 1),
        (left + width / 2, top + height - 1),
        (left + width - 1, top + height - 1)
    ]
    return pointer
