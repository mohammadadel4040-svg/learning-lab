import logging
from collections import defaultdict

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("analysis_audit.log"),
        logging.StreamHandler()
    ]
)


failed_attempts = defaultdict(int)
security_incidents = []
errors = []


def analyze_log():

    try:
        with open("server.log", "r") as file:

            for line in file:

                if "Forbidden access" in line:
                    security_incidents.append(line)
                    logging.warning(line.strip())

                if "SQL injection" in line:
                    security_incidents.append(line)
                    logging.warning(line.strip())

                if "Brute force" in line:
                    security_incidents.append(line)
                    logging.warning(line.strip())

                if "ERROR" in line:
                    errors.append(line)

        generate_reports()

    except FileNotFoundError:
        logging.error("server.log not found")


def generate_reports():

    with open("security_incidents.txt", "w") as sec:
        sec.write("SECURITY INCIDENTS\n")
        sec.write("=" * 50 + "\n")
        for incident in security_incidents:
            sec.write(incident)

    with open("error_log.txt", "w") as err:
        err.write("ERROR LOGS\n")
        err.write("=" * 50 + "\n")
        for error in errors:
            err.write(error)

    print("Analysis Complete")
    print("Security incidents:", len(security_incidents))
    print("Errors:", len(errors))


if __name__ == "__main__":
    analyze_log()
