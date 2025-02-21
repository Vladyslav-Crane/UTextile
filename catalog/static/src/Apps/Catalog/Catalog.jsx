import React from "react";
import "./catalog.css";

function Catalog() {
  return (
    <div className="catalog-container">
      {/* Левая колонка (фильтры) */}
      <aside className="filters">
        <h2>Категории</h2>
        <ul>
          <li>
            <label>
              <input type="checkbox" />
              Новый год
            </label>
          </li>
          <li>
            <label>
              <input type="checkbox" />
              Спальня
            </label>
          </li>
          <li>
            <label>
              <input type="checkbox" />
              Ванная комната
            </label>
          </li>
          <li>
            <label>
              <input type="checkbox" />
              Кухня и столовая
            </label>
          </li>
          <li>
            <label>
              <input type="checkbox" />
              Декоративный текстиль
            </label>
          </li>
          <li>
            <label>
              <input type="checkbox" />
              Декор для дома
            </label>
          </li>
          <li>
            <label>
              <input type="checkbox" />
              Свечи и ароматы
            </label>
          </li>
          <li>
            <label>
              <input type="checkbox" />
              Коллекция из шёлка
            </label>
          </li>
          <li>
            <label>
              <input type="checkbox" />
              Сертификаты
            </label>
          </li>
        </ul>

        <h2>Коллекция</h2>
        <ul>
          <li>
            <label>
              <input type="checkbox" />
              Essential (428)
            </label>
          </li>
          <li>
            <label>
              <input type="checkbox" />
              Edge (196)
            </label>
          </li>
          <li>
            <label>
              <input type="checkbox" />
              Ethnic (122)
            </label>
          </li>
          <li>
            <label>
              <input type="checkbox" />
              New Year Essential (82)
            </label>
          </li>
          <li>
            <label>
              <input type="checkbox" />
              Scandinavian touch (35)
            </label>
          </li>
          {/* ... другие пункты */}
        </ul>

        <h2>Цвет</h2>
        <ul>
          <li>
            <label>
              <input type="checkbox" />
              Бежевый (184)
            </label>
          </li>
          <li>
            <label>
              <input type="checkbox" />
              Серый (155)
            </label>
          </li>
          {/* ... другие пункты */}
        </ul>
      </aside>

      {/* Правая колонка (список товаров) */}
      <main className="products">
        <h1>Каталог домашнего текстиля</h1>

        {/* Дополнительные элементы управления: сортировка, чекбокс "Товар в наличии" и т.д. */}
        <div className="products-controls">
          <div>
            <label htmlFor="collection-select">По коллекциям</label>
            <select id="collection-select">
              <option value="">Все коллекции</option>
              <option value="Essential">Essential</option>
              <option value="Edge">Edge</option>
              {/* ... */}
            </select>
          </div>
          <div>
            <label>
              <input type="checkbox" />
              Товар в наличии
            </label>
          </div>
          {/* Количество товаров (пример) */}
          <div>1065 товаров</div>
        </div>

        {/* Сетка с карточками товаров */}
        <div className="products-grid">
          <div className="product-card">
            <img
              src="https://via.placeholder.com/250x300?text=Пример+товара"
              alt="Пример товара"
            />
            <div>
              <span className="discount-label">-25%</span>
              <span className="old-price">7 990 ₽</span>
            </div>
            <h3 className="price">5 993 ₽</h3>
            <p>Плед из хлопка с рисунком Tulip Garden из коллекции Terra</p>
            <button>Купить</button>
          </div>

          <div className="product-card">
            <img
              src="https://via.placeholder.com/250x300?text=Пример+товара"
              alt="Пример товара"
            />
            <div>
              <span className="discount-label">-10%</span>
              <span className="old-price">5 000 ₽</span>
            </div>
            <h3 className="price">4 500 ₽</h3>
            <p>Набор полотенец для ванной (бежевый)</p>
            <button>Купить</button>
          </div>

          {/* ... Другие карточки */}
        </div>
      </main>
    </div>
  );
}

export default Catalog;
