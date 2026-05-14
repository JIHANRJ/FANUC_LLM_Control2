"""Voice engine package for speech-to-text using Whisper."""

from . import voice_settings

__all__ = ["voice_settings", "VoiceInput"]


def __getattr__(name):
	if name == "VoiceInput":
		from .voice_input import VoiceInput

		return VoiceInput
	raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
