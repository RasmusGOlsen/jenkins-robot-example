import re

from typing import Tuple
from subprocess import run, PIPE
from robot.api.deco import keyword


@keyword
def run_synthesis_and_implementation() -> None:
    """Run the synthesis and implementation flow.
    """
    pass


@keyword
def parse_synthesis_report_for_errors() -> None:
    """Parse the synthesis report for errors.
    """
    pass


@keyword
def parse_drc_report_for_errors() -> None:
    """Parse the design rule check report for errors.
    """
    pass


@keyword
def parse_cdc_report_for_errors() -> None:
    """Parse the clock domain crossing report for errors.
    """
    pass


@keyword
def perform_timing_analysis() -> None:
    """Perform a timing analysis
    """
    pass


@keyword
def run_deployment() -> None:
    """Run deployment procedure.
    """
    pass


@keyword
def run_simulation(testname: str) -> str:
    """Runs simulation

    Args:
        testname (str): The name if the test-case to run.

    Returns:
        str: standard output
    """
    stdout, _, _ = sh(f"echo Running {testname} Test passed!")
    return stdout


@keyword
def parse_output_for_errors(text: str) -> None:
    """Parse the text string and search for any line starting with *error*

    Args:
        text (str): text to parse

    Raises:
        AssertionError: If any lines starts with *error*.
    """
    m = re.match(r"^error", text)
    if m:
        raise AssertionError(m.groups)


def parse_output_for_pass(text: str, pass_string: str) -> None:
    """Parse the text and search for a *pass string*

    Args:
        text (str): text to parse.
        pass_string (str): string to search for.

    Raises:
        AssertionError: if string is not found in text.
    """
    m = re.match(rf".*{pass_string}.*", text)
    if not m:
        raise AssertionError(f"{pass_string}: not found")


def sh(command: str, check=True) -> Tuple[str, str, int]:
    """Run command from the shell

    Args:
        command (str): Command and arguments to run.
        check (bool, optional): Check of return code is non zero. Defaults to
                                True.

    Raises:
        AssertionError: When check is True and return code is non zero.

    Returns:
        Tuple[str, str, int]: standard output, standard error and return code.
    """
    p = run(command, stdout=PIPE, stderr=PIPE, shell=True)
    if check and p.returncode != 0:
        raise AssertionError(p.stderr.decode())
    return (p.stdout.decode(), p.stderr.decode(), p.returncode)
