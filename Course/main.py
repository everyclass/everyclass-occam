# coding=utf-8
import Config
import Common
import Room.database as dao


def main(config, semester, version):
    # 更新全体名单
    tag_meaning = {
        "序号": "id",
        "课程号": "code",
        "课程名称": "name",
        "课程大类": "type",
        "开课单位": "faculty",
    }
    if Common.fetch_list_data(config, version, "课程列表", "course", tag_meaning, "kcmd", 100):
        Common.merge_page_info(config, version, "课程列表", "course", dao.write_room_info)

    # 更新活跃教室
    active_list = Common.fetch_active_list(config, version, "可用课程", "act_course", "kclb", semester)

    # 更新教室课表
    Common.fetch_class_table(_config, version, "课程课表", "course_table", "kckb", "2019-2020-1", active_list)
    Common.merge_table_info(_config, version, "课程课表", "course_table", "room")


if __name__ == "__main__":
    _config = Config.load_config("../Config")
    main(_config, "2019-2020-1", "2019-11-27")