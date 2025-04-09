from feedback_summary import show_summary

def test_show_summary(capfd):
    feedback_data = [
        {"name": "Alice", "score": 90, "feedback": "Great!"},
        {"name": "Bob", "score": 75, "feedback": "Needs improvement"}
    ]
    show_summary(feedback_data)
    out, _ = capfd.readouterr()
    assert "Alice (90): Great!" in out
    assert "Bob (75): Needs improvement" in out
