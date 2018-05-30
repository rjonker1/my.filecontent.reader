import re

log_path = '.\\2018-05-25-UsBankPivotPrivate.log'
with open(log_path) as log_file:
    # read the log file
    line = log_file.readline()
    count = 1
    while line:
        extracted_pattern = re.compile(r'(.*)Found (\d{1}) Reports Extracted From Deal Report ID (\d{8}). Will Skip Deleting this Report.')
        success_deleted_pattern = re.compile(r'(.*)(\d{1,}) were successfully deleted.')
        matched_extracted = extracted_pattern.match(line.strip())
        if matched_extracted:
            print(f"{matched_extracted.groups()[1]} - {matched_extracted.groups()[2]}")

        matched_success = success_deleted_pattern.match(line.strip())
        if matched_success:
            print(f"{matched_success.groups()[1]} deleted")

        line = log_file.readline()
