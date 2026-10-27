# Configuration loading

load_config accepts an absolute or relative path to a JSON configuration file. The configuration contains template_file. A relative template_file must be resolved against the configuration file's directory, regardless of the process working directory. An absolute template_file must be used unchanged. Return the configuration fields with an additional template_text field containing the UTF-8 template contents. Do not change the process working directory.

Repair app.py only. Preserve the existing public function signatures. Run the provided recorder before editing and after each repair attempt.
