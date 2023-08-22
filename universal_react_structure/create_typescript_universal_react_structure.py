# create_universal_react_structure.py

import os

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file_with_comment(path, comment):
    if path.endswith((".ts", ".tsx", ".html", ".css")):
        with open(path, 'w', encoding='utf-8') as file:
            file.write(comment)

def create_empty_file(path):
    with open(path, 'wb') as file:
        pass

def create_project_structure():
    base_path = "D:/projects/universal_react_structure/"
    base_dir = os.path.join(base_path, "universal_react_structure/src/")
    create_folder(os.path.join(base_dir, "assets/images"))
    create_empty_file(os.path.join(base_dir, "assets/images/avatar.jpg"))
    create_empty_file(os.path.join(base_dir, "assets/images/logo.png"))
    create_empty_file(os.path.join(base_dir, "assets/images/background.jpg"))
    create_folder(os.path.join(base_dir, "assets/icons"))
    create_empty_file(os.path.join(base_dir, "assets/icons/facebook.svg"))
    create_empty_file(os.path.join(base_dir, "assets/icons/twitter.svg"))
    create_empty_file(os.path.join(base_dir, "assets/icons/instagram.svg"))
    # ... продолжение для остальных файлов и папок
    create_folder(base_dir + "components/Auth")
    create_file_with_comment(base_dir + "components/Auth/AuthProvider.tsx", "// Контекст аутентификации пользователя.")
    create_file_with_comment(base_dir + "components/Auth/Login.tsx", "// Компонент для входа пользователя.")
    create_file_with_comment(base_dir + "components/Auth/Register.tsx", "// Компонент для регистрации пользователя.")
    create_file_with_comment(base_dir + "components/Auth/SocialLogin.tsx", "// Компонент для входа через социальные сети.")

    # Дополнительные части
    create_folder(base_dir + "components/UserProfile")
    create_file_with_comment(base_dir + "components/UserProfile/UserProfile.tsx", "// Основной компонент профиля пользователя.")
    create_file_with_comment(base_dir + "components/UserProfile/Avatar.tsx", "// Компонент для отображения аватара пользователя.")
    create_file_with_comment(base_dir + "components/UserProfile/Bio.tsx", "// Компонент для отображения биографической информации.")

    create_folder(base_dir + "components/Settings")
    create_file_with_comment(base_dir + "components/Settings/Settings.tsx", "// Компонент настроек пользователя.")
    create_file_with_comment(base_dir + "components/Settings/Notifications.tsx", "// Компонент для управления уведомлениями.")
    create_file_with_comment(base_dir + "components/Settings/InterfaceSettings.tsx", "// Компонент настроек интерфейса.")

    create_folder(base_dir + "components/Messaging")
    create_file_with_comment(base_dir + "components/Messaging/Messages.tsx", "// Основной компонент для просмотра сообщений.")
    create_file_with_comment(base_dir + "components/Messaging/Chat.tsx", "// Компонент для чата.")
    create_file_with_comment(base_dir + "components/Messaging/MessageInput.tsx", "// Компонент для ввода сообщений.")
    create_file_with_comment(base_dir + "components/Messaging/ConversationList.tsx", "// Компонент для списка бесед.")

    create_folder(base_dir + "components/AdminPanel")
    create_file_with_comment(base_dir + "components/AdminPanel/AdminDashboard.tsx", "// Основной компонент панели администратора.")
    create_file_with_comment(base_dir + "components/AdminPanel/UserManagement.tsx", "// Компонент для управления пользователями.")
    create_file_with_comment(base_dir + "components/AdminPanel/ContentManagement.tsx", "// Компонент для управления контентом.")

    create_folder(base_dir + "components/Shared")
    create_file_with_comment(base_dir + "components/Shared/Button.tsx", "// Общий компонент кнопки.")
    create_file_with_comment(base_dir + "components/Shared/Input.tsx", "// Общий компонент ввода.")
    create_file_with_comment(base_dir + "components/Shared/Dropdown.tsx", "// Общий компонент выпадающего списка.")
    # ... и так далее для всех остальных папок и файлов

    create_folder(base_dir + "contexts")
    create_file_with_comment(base_dir + "contexts/AuthContext.ts", "// Контекст аутентификации.")
    create_folder(base_dir + "hooks")
    create_file_with_comment(base_dir + "hooks/useAuth.ts", "// Кастомный хук для работы с аутентификацией.")
    create_file_with_comment(base_dir + "hooks/useApi.ts", "// Кастомный хук для работы с API.")
    create_folder(base_dir + "services")
    create_file_with_comment(base_dir + "services/api.ts", "// Сервис для обращения к API.")
    create_file_with_comment(base_dir + "services/auth.ts", "// Сервис для работы с аутентификацией.")
    create_folder(base_dir + "styles")
    create_file_with_comment(base_dir + "styles/GlobalStyles.ts", "// Глобальные стили.")
    create_folder(base_dir + "styles/componentStyles")
    create_file_with_comment(base_dir + "styles/componentStyles/AuthStyles.ts", "// Стили для компонентов аутентификации.")
    # Добавьте остальные файлы стилей сюда

    create_folder(os.path.join(base_dir, "utils"))
    create_file_with_comment(os.path.join(base_dir, "utils/helpers.ts"), "// Вспомогательные функции.")
    create_file_with_comment(os.path.join(base_dir, "utils/formatDate.ts"), "// Функция для форматирования дат.")
    create_file_with_comment(os.path.join(base_dir, "utils/validation.ts"), "// Функции для валидации данных.")

    create_folder(os.path.join(base_dir, "routes"))
    create_file_with_comment(os.path.join(base_dir, "routes/PrivateRoute.tsx"), "// Приватный маршрут для авторизованных пользователей.")
    create_file_with_comment(os.path.join(base_dir, "routes/PublicRoute.tsx"), "// Публичный маршрут для всех пользователей.")

    create_folder(os.path.join(base_dir, "config"))
    create_file_with_comment(os.path.join(base_dir, "config/config.ts"), "// Конфигурационные параметры приложения.")

    create_folder(os.path.join(base_dir, "tests"))
    create_file_with_comment(os.path.join(base_dir, "tests/Auth.test.ts"), "// Тесты для компонентов аутентификации.")
    # Добавьте остальные файлы тестов сюда

    create_file_with_comment(os.path.join(base_dir, "App.tsx"), "// Основной компонент приложения, определяет маршрутизацию.")
    create_file_with_comment(os.path.join(base_dir, "index.tsx"), "// Точка входа в приложение.")

    create_folder("my-app/public")
    create_file_with_comment("my-app/public/index.html", "// Главный HTML файл.")

    print("Структура проекта успешно создана!")

if __name__ == "__main__":
    create_project_structure()