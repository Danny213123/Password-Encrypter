import base64

Hidden = "CmltcG9ydCBtYXRoCmltcG9ydCByYW5kb20KCmQsIGogPSBpbnQobWF0aC5sb2cobWF0aC5wb3cobWF0aC5lLCBvcmQoIiAiKSksIG1hdGguZSkpLCBpbnQobWF0aC5sb2cobWF0aC5wb3cobWF0aC5lLCAob3JkKCIgIikgKiAzLjk2ODc1KSksIG1hdGguZSkpCmEsIGIgPSAoZCkudG9fYnl0ZXMoMiwgYnl0ZW9yZGVyPSdsaXR0bGUnKSwgKGopLnRvX2J5dGVzKDIsIGJ5dGVvcmRlcj0nbGl0dGxlJykKClN0b3JhZ2UgPSB7fQoKZGVmIEVuY3J5cHQoV29yZCk6CgoJRW5jcnlwdGVkID0gIiIKCglmb3IgeCBpbiByYW5nZSgxLCBsZW4oV29yZCkgKyAxKToKCgkJQVNDSUkgPSBvcmQoV29yZFt4IC0gMV0pCgoJCWlmICh4ICUgMiA9PSAxKToKCgkJCUNoZWNrID0gQVNDSUkgLSB4CgoJCQlpZiAoQ2hlY2sgPCBpbnQuZnJvbV9ieXRlcyhhLCAibGl0dGxlIikpOgoKCQkJCUVuY3J5cHRlZCArPSBjaHIoaW50LmZyb21fYnl0ZXMoYiwgImxpdHRsZSIpIC0gKHggLSAoQVNDSUkgLSBpbnQuZnJvbV9ieXRlcyhhLCAibGl0dGxlIikpKSkKCgkJCWVsc2U6CgoJCQkJRW5jcnlwdGVkICs9IGNocihBU0NJSSAtIHgpCgoJCWVsc2U6CgoJCQlDaGVjayA9IEFTQ0lJICsgeAoKCQkJaWYgKENoZWNrID4gaW50LmZyb21fYnl0ZXMoYiwgImxpdHRsZSIpKToKCgkJCQlFbmNyeXB0ZWQgKz0gY2hyKGludC5mcm9tX2J5dGVzKGEsICJsaXR0bGUiKSArICh4ICsgKEFTQ0lJIC0gaW50LmZyb21fYnl0ZXMoYiwgImxpdHRsZSIpKSkpCgoJCQllbHNlOgoKCQkJCUVuY3J5cHRlZCArPSBjaHIoQVNDSUkgKyB4KQoKCXJldHVybiBFbmNyeXB0ZWQKCgpkZWYgRGVjcnlwdChXb3JkKToKCglEZWNyeXB0ZWQgPSAiIgoKCWZvciB4IGluIHJhbmdlKDEsIGxlbihXb3JkKSArIDEpOgoKCQlDaGFyID0gb3JkKFdvcmRbeCAtIDFdKQoKCQlpZiAoeCAlIDIgPT0gMSk6CgoJCQlDaGVjayA9IENoYXIgKyB4CgoJCQlpZiAoQ2hlY2sgPiBpbnQuZnJvbV9ieXRlcyhiLCAibGl0dGxlIikpOgoKCQkJCURlY3J5cHRlZCArPSBjaHIoaW50LmZyb21fYnl0ZXMoYSwgImxpdHRsZSIpICsgKENoYXIgLSAoaW50LmZyb21fYnl0ZXMoYiwgImxpdHRsZSIpIC0geCkpKQoKCQkJZWxzZToKCgkJCQlEZWNyeXB0ZWQgKz0gY2hyKENoYXIgKyB4KQoKCQllbHNlOgoKCQkJQ2hlY2sgPSBDaGFyIC0geAoKCQkJaWYgKENoZWNrIDwgaW50LmZyb21fYnl0ZXMoYSwgImxpdHRsZSIpKToKCgkJCQlEZWNyeXB0ZWQgKz0gY2hyKGludC5mcm9tX2J5dGVzKGIsICJsaXR0bGUiKSAtICh4IC0gKENoYXIgLSBpbnQuZnJvbV9ieXRlcyhhLCAibGl0dGxlIikpKSkKCgkJCWVsc2U6CgoJCQkJRGVjcnlwdGVkICs9IGNocihDaGFyIC0geCkKCglyZXR1cm4gRGVjcnlwdGVkCgpkZWYgbWFpbigpOgoKCWNob2ljZSA9IGlucHV0KCJSZXRyaXZlIG9yIGVudGVyIGEgbmV3IHZhbHVlPyAoUiBvciBOKTogIikKCglpZiAoY2hvaWNlID09ICJSIik6CgkJZGVjcnlwdCA9IGlucHV0KCJFbnRlciB0aGUgZW5jcnlwdGVkIHZhbHVlOiAiKQoJCWtleSA9IGludChpbnB1dCgiRW50ZXIgdGhlIGtleTogIikpCgkJZm9yIHggaW4gcmFuZ2UgKGtleSk6CgkJCWRlY3J5cHQgPSBEZWNyeXB0KGRlY3J5cHQpCgkJcHJpbnQoIllvdXIgZGVjcnlwdGVkIG1lc3NhZ2UgaXMgIiwgZGVjcnlwdCkKCWVsc2U6CgkJa2V5ID0gcmFuZG9tLnJhbmRpbnQoMTAwLCA5OTk5OSkKCQllbmNyeXB0ID0gaW5wdXQoIkVudGVyIGEgdmFsdWU6ICIpCgkJZm9yIHggaW4gcmFuZ2UgKGtleSk6CgkJCWVuY3J5cHQgPSBFbmNyeXB0KGVuY3J5cHQpCgkJcHJpbnQoIllvdXIga2V5IGlzOiAiLCBrZXksICIgYW5kIHlvdXIgZW5jcnlwdGVkIG1lc3NhZ2UgaXM6ICIsIGVuY3J5cHQpCgkKCm1haW4oKQo="

eval(compile(base64.b64decode(Hidden).decode(), '<string', 'exec'))
