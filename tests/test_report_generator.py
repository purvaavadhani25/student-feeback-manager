from report_generator import generate_report

def test_generate_report(tmp_path):
    feedback_data = [
        {"name": "Charlie", "score": 85, "feedback": "Nice work"}
    ]
    file_path = tmp_path / "test_report.txt"
    generate_report(feedback_data, filename=file_path)
    
    assert file_path.exists()
    content = file_path.read_text()
    assert "Charlie" in content
    assert "85" in content
    assert "Nice work" in content
