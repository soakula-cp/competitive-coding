import logging
import math
import os
import shutil
from datetime import date
from typing import List

from lib.problem.base import Problem
from lib.utils.enums import WriteContentEnum
from lib.utils.functions import create_empty_file, create_directory


class BaseFileWrite(object):
    def __init__(self,
                 template_root_directory: str,
                 solution_copyright: bool = True,
                 solution_file_description: bool = True,
                 solution_changelog: bool = True,
                 solution_include_and_using: bool = True,
                 solution_base_class: bool = True,
                 solution_implementation: bool = True,
                 solution_main: bool = True,
                 description_header: bool = True,
                 description_body: bool = True):
        """

        Args:
            template_root_directory: Directory containing template files
            solution_copyright: Should the solution file have copyright in
                                header? Default: True
            solution_file_description: Should the solution file have file
                                       description in header? Default: True
            solution_changelog: Should the solution file have changelog in
                                header? Default: True
            solution_include_and_using: Should the solution file have
                                        include header and using? Default: True
            solution_base_class: Should the solution file have base class?
                                 Default: True
            solution_implementation: Should the solution file have default
                                     implementation of base class? Default: True
            solution_main: Should the solution file have main()? Default: True
            description_header: Should the description file have yaml header?
                                Default: True
            description_body: Should the description file have problem related
                              info? Default: True
        """
        self.write_solution = [
            (solution_copyright, 'copyright-notice.cpp'),
            (solution_file_description, 'file-description.cpp'),
            (solution_changelog, 'changelog.cpp'),
            (solution_include_and_using, 'include_and_using.cpp'),
            (solution_base_class, 'solution-base.cpp'),
            (solution_implementation, 'solution-implement.cpp'),
            (solution_main, 'main.cpp')
        ]
        self.write_description = [
            (description_header, 'description-header.md'),
            (description_body, 'description-body.md')
        ]
        self.template_root_directory = template_root_directory

    def create_file_for_problem(
        self,
        problem: Problem,
        root_directory: str,
        write_type: WriteContentEnum,
        should_overwrite: bool = False) -> (bool, str):
        """
        Create a file based on write_type for the problem in root_directory
        Args:
            problem: problem for which the file needs to be created
            root_directory: Root directory in which the file needs to be created
            write_type: Type of the file to write
            should_overwrite: If the file already exists, should it be
                              overwritten? Default: False

        Returns:
            bool - True if the file has created/updated else False
            List[str] - content from the file which has been created/updated
        """
        template_file_path = \
            self.template_root_directory + problem.get_template_filename(
                write_type)
        print(template_file_path)
        logging.debug(f"Template file path (relative): {template_file_path}")
        template_file_path = os.path.relpath(template_file_path)
        logging.debug(f"Template file path (absolute): {template_file_path}")
        self.create_template_file(
            template_file_path, problem, write_type,
            should_overwrite=should_overwrite)
        output_file_path = \
            root_directory + \
            ('/' if root_directory[:-1] != '/' else '') + \
            problem.get_output_filename(write_type=write_type)
        _, _ = \
            self.check_if_file_exists_for_problem(output_file_path,
                                                  template_file_path)
        if os.path.exists(output_file_path) and not should_overwrite:
            print("File already setup for {0} for {1}. {2} at {3}".format(
                str(write_type), problem.identifier, problem.title,
                os.path.abspath(output_file_path)))
            return False, output_file_path
        print("Setting up default {0} for {1}. {2} at {3} using {4}"
              .format(str(write_type), problem.identifier, problem.title,
                      output_file_path, template_file_path))
        create_empty_file(output_file_path)
        if not os.path.exists(template_file_path):
            self.create_template_file(template_file_path, problem, write_type)
        shutil.copy(template_file_path, output_file_path)
        return True, output_file_path

    @staticmethod
    def update_file_line(line: str, problem: Problem) -> str:
        """

        Args:
            line:
            problem:

        Returns:

        """
        today = date.today()
        year = today.strftime("%Y")
        expanded_date = today.strftime("%d %B %Y")
        short_date = today.strftime("%d-%m-%Y")
        author_alias = "sonapraneeth_a"
        author_name = "Sona Praneeth Akula"
        author_email = "sonapraneeth.akula@gmail.com"
        problem_directory = problem.problem_directory
        problem_id = str(problem.identifier)
        problem_url = problem.problem_url
        problem_title = problem.title
        update_line = line
        # Copyright Notice
        if "TEMPLATE__YEAR" in update_line:
            update_line = update_line.replace("TEMPLATE__YEAR", year)
        if "TEMPLATE__AUTHOR_ALIAS" in update_line:
            update_line = update_line.replace("TEMPLATE__AUTHOR_ALIAS",
                                              author_alias)
        if "TEMPLATE__AUTHOR_NAME" in update_line:
            update_line = update_line.replace("TEMPLATE__AUTHOR_NAME",
                                              author_name)
        if "TEMPLATE__AUTHOR_EMAIL" in update_line:
            update_line = update_line.replace("TEMPLATE__AUTHOR_EMAIL",
                                              author_email)
        if "TEMPLATE__JUDGE" in update_line:
            update_line = update_line.replace("TEMPLATE__JUDGE",
                                              str(problem.judge))
        if "TEMPLATE__EXPLORE_NAME" in update_line:
            update_line = update_line.replace("TEMPLATE__EXPLORE_NAME",
                                              str(problem.explore_identifier))
        if "TEMPLATE__CONTEST_NAME" in update_line:
            update_line = update_line.replace("TEMPLATE__CONTEST_NAME",
                                              str(problem.contest_identifier))
        # Changelog
        if "TEMPLATE__SHORT_DATE" in update_line:
            update_line = update_line.replace("TEMPLATE__SHORT_DATE",
                                              short_date)
        # File Description
        if "TEMPLATE__PROBLEM_DIRECTORY" in update_line:
            update_line = \
                update_line.replace("TEMPLATE__PROBLEM_DIRECTORY",
                                    problem_directory)
        if "TEMPLATE__COMPILE_COMMAND" in update_line:
            update_line = \
                update_line.replace("TEMPLATE__COMPILE_COMMAND",
                                    problem.compile_command)
        if "TEMPLATE__EXPANDED_DATE" in update_line:
            update_line = update_line.replace("TEMPLATE__EXPANDED_DATE",
                                              expanded_date)
        if "TEMPLATE__PROBLEM_TITLE" in update_line:
            update_line = update_line.replace("TEMPLATE__PROBLEM_TITLE",
                                              problem_title)
        # Description header
        if "TEMPLATE__PROBLEM_ID" in update_line:
            update_line = \
                update_line.replace("TEMPLATE__PROBLEM_ID", problem_id)
        if "TEMPLATE__PROBLEM_URL" in update_line:
            update_line = \
                update_line.replace("TEMPLATE__PROBLEM_URL", problem_url)
        if "TEMPLATE__PROBLEM_DIFFICULTY_COLOR" in update_line:
            update_line = update_line.replace(
                "TEMPLATE__PROBLEM_DIFFICULTY_COLOR", problem.difficulty_color)
        if "TEMPLATE__PROBLEM_DIFFICULTY" in update_line:
            update_line = update_line.replace("TEMPLATE__PROBLEM_DIFFICULTY",
                                              str(problem.difficulty))
        return update_line

    @staticmethod
    def get_template_part_file_info(
        problem: Problem,
        filename: str,
        file_handle: any) -> (str, List[str]):
        """

        Args:
            problem:
            filename:
            file_handle:

        Returns:

        """
        directory_list = [
            f"{str(problem.judge).lower()}/{str(problem.source_type).lower()}/",
            f"{str(problem.judge).lower()}/",
            f"base/{str(problem.source_type).lower()}/",
            f"base/"
        ]
        path, is_part_template_present = "", False
        for directory in directory_list:
            path = "./templates/" + directory + filename
            if os.path.exists(path):
                is_part_template_present = True
                break
        if not is_part_template_present:
            print(f"{problem.judge} template missing for {filename}")
            exit(1)
        template_file_handle = open(path, "r")
        lines = template_file_handle.readlines()
        file_handle.writelines(lines)
        file_handle.write("\n")
        template_file_handle.close()
        return "", lines

    def create_template_file(
        self,
        filename: str,
        problem: Problem,
        write_type: WriteContentEnum,
        should_overwrite: bool = False) -> bool:
        """

        Args:
            filename:
            problem:
            write_type:
            should_overwrite:

        Returns:

        """
        if not should_overwrite and os.path.exists(filename):
            return False
        create_directory(os.path.dirname(filename))
        file_handle = open(filename, "w")
        if write_type == WriteContentEnum.SOLUTION:
            for (to_write, filename) in self.write_solution:
                if to_write:
                    self.get_template_part_file_info(problem, filename,
                                                     file_handle)
        elif write_type == WriteContentEnum.DESCRIPTION:
            for (to_write, filename) in self.write_description:
                if to_write:
                    self.get_template_part_file_info(problem, filename,
                                                     file_handle)
        file_handle.close()
        return True

    @staticmethod
    def check_if_file_exists_for_problem(
        output_file_path: str,
        template_file_path: str) -> (bool, bool, str):
        """

        Args:
            output_file_path:
            template_file_path:

        Returns:

        """
        template_file_path_size = os.path.getsize(template_file_path)
        template_file_size = math.ceil(2.25 * template_file_path_size)
        is_attempted, is_existing = False, False
        if os.path.exists(output_file_path):
            is_existing = True
            if os.path.getsize(output_file_path) >= template_file_size:
                # print("Template filepath: {0}, size: {1}"
                #       .format(template_file_path, template_file_size))
                # print("Output file path: {0}, size: {1}"
                #       .format(output_file_path,
                #               os.path.getsize(output_file_path)))
                # print("File size: {0} {1}".format(
                #     problem_directory, os.path.getsize(output_file_path)))
                is_attempted = True
        return is_existing, is_attempted
